import grpc
import jwt
from grpc import ServicerContext
from grpc_interceptor import AsyncServerInterceptor

import src.server.internal.auth.entities.jwt_blacklist as jwt_blacklist

ignoreEndpoints = ["/auth.v1.AuthService/SignUp", "/auth.v1.AuthService/SignIn"]


class JWTAuthInterceptor(AsyncServerInterceptor):
    def __init__(self, secret_key):
        self.secret_key = secret_key

    async def intercept(self, method, request, context, method_name):
        if method_name in ignoreEndpoints:
            return await method(request, context)

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
            jwt.decode(auth_token, self.secret_key, algorithms=["HS256"])

        # NOTE: The ExpiredSignatureError MUST be caught before the InvalidTokenError
        except jwt.ExpiredSignatureError:
            await self.abort_with_unauthenticated(context, "Token has expired")

        except jwt.InvalidTokenError:
            await self.abort_with_unauthenticated(context, "Invalid token")

        # Proceed with the gRPC method invocation
        # NOTE: EVERY routes defined MUST be an async function
        return await method(request, context)

    async def abort_with_unauthenticated(self, context: ServicerContext, message: str):
        await context.abort(grpc.StatusCode.UNAUTHENTICATED, message)
