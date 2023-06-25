import grpc
import jwt
from grpc import ServicerContext
from grpc_interceptor import AsyncServerInterceptor
from grpc_interceptor.exceptions import GrpcException

import src.server.internal.auth.entities.jwt_blacklist as jwt_blacklist
import src.server.internal.auth.services.interceptor.custom_context as custom_context

ignoreEndpoints = ["/auth.v1.AuthService/SignUp", "/auth.v1.AuthService/SignIn"]


class JWTAuthInterceptor(AsyncServerInterceptor):
    def __init__(self, secret_key):
        self.secret_key = secret_key

    async def intercept(self, method, request, context, method_name):
        if method_name in ignoreEndpoints:
            return await self.handleRequest(method, request, context)

        auth_metadata = dict(context.invocation_metadata())
        if "authorization" not in auth_metadata:
            await self.abort_with_unauthenticated(
                context, "Missing authorization token"
            )

        auth_header = auth_metadata["authorization"]
        auth_scheme, auth_token = auth_header.split(" ")
        if auth_scheme.lower() != "bearer":
            await self.abort_with_unauthenticated(
                context, "Invalid authorization scheme"
            )

        if not auth_token:
            await self.abort_with_unauthenticated(context, "Empty authorization token")

        isBlacklisted = await jwt_blacklist.JWTBlacklist.exists(token=auth_token)

        if isBlacklisted:
            await self.abort_with_unauthenticated(context, "Token has been revoked")

        try:
            # Verify and decode the token
            decoded_token = jwt.decode(
                auth_token, self.secret_key, algorithms=["HS256"]
            )

            userId = decoded_token["user_id"]

            # Add the user_id to the context
            extra_context = {"user_id": userId}

            # NOTE: Construct a new context with the extra_context
            context = custom_context.CustomContext(context, extra_context)

        # NOTE: The ExpiredSignatureError MUST be caught before the InvalidTokenError
        except jwt.ExpiredSignatureError:
            await self.abort_with_unauthenticated(context, "Token has expired")

        except jwt.InvalidTokenError:
            await self.abort_with_unauthenticated(context, "Invalid token")

        # Proceed with the gRPC method invocation
        # NOTE: EVERY routes defined MUST be an async function
        return await self.handleRequest(method, request, context)

    async def abort_with_unauthenticated(self, context: ServicerContext, message: str):
        await context.abort(grpc.StatusCode.UNAUTHENTICATED, message)

    # Ref: https://grpc-interceptor.readthedocs.io/en/latest/#async-server-interceptors
    async def handleRequest(self, method, request, context):
        try:
            response_or_iterator = method(request, context)
            if not hasattr(response_or_iterator, "__aiter__"):
                # Unary, just await and return the response
                return await response_or_iterator
        except GrpcException as e:
            await context.set_code(e.status_code)
            await context.set_details(e.details)
            raise

        # Server streaming responses, delegate to an async generator helper.
        # Note that we do NOT await this.
        return self._intercept_streaming(response_or_iterator, context)

    # Ref: https://grpc-interceptor.readthedocs.io/en/latest/#async-server-interceptors
    async def _intercept_streaming(self, iterator, context):
        try:
            async for r in iterator:
                yield r
        except GrpcException as e:
            await context.set_code(e.status_code)
            await context.set_details(e.details)
            raise
