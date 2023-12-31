import jwt

import src.server.internal.auth.entities.jwt_blacklist as jwt_blacklist
import src.server.internal.auth.entities.user as user
import src.server.server as server
import src.shared.interceptor.base_interceptor as base_interceptor
import src.shared.interceptor.custom_context as custom_context

ignoreEndpoints = ["/auth.v1.AuthService/SignUp", "/auth.v1.AuthService/SignIn"]


class JWTAuthInterceptor(base_interceptor.BaseInterceptor):
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

            isUserExists = await user.User.exists(id=userId)

            if not isUserExists:
                await self.abort_with_unauthenticated(context, "User not found")

            # Add the user_id to the context
            extra_context = {"user_id": userId}

            # NOTE: Construct a new context with the extra_context
            context = custom_context.CustomContext(context, extra_context)

            # NOTE: Increase the number of clients
            await server.server.clientPool.add(user_id=userId)

        # NOTE: The ExpiredSignatureError MUST be caught before the InvalidTokenError
        except jwt.ExpiredSignatureError:
            await self.abort_with_unauthenticated(context, "Token has expired")

        except jwt.InvalidTokenError:
            await self.abort_with_unauthenticated(context, "Invalid token")

        # Proceed with the gRPC method invocation
        # NOTE: EVERY routes defined MUST be an async function
        return await self.handleRequest(method, request, context)
