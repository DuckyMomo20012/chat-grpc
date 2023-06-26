import datetime

import grpc
import jwt
import tortoise.exceptions

import pkg.protobuf.auth_service.auth_service_pb2 as auth_service_pb2
import pkg.protobuf.auth_service.auth_service_pb2_grpc as auth_service_pb2_grpc
import src.server.internal.auth.entities.jwt_blacklist as jwt_blacklist
import src.server.internal.auth.entities.user as user
import src.server.server as server


class AuthService(auth_service_pb2_grpc.AuthServiceServicer):
    async def SignUp(self, request, context):
        isExisted = await user.User.exists(user_name=request.user_name)

        if isExisted:
            context.set_details("User already exists")
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            return auth_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        else:
            newUser = await user.User.create(
                user_name=request.user_name, password=request.password
            )

            return auth_service_pb2.SignUpResponse(user_id=f"{newUser.id}")

    async def SignIn(self, request, context):
        try:
            currUser = await user.User.get(user_name=request.user_name)
        except tortoise.exceptions.DoesNotExist:
            context.set_details("User does not exist")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return auth_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

        if currUser.password != request.password:
            context.set_details("Password is incorrect")
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            return auth_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

        accessToken = jwt.encode(
            {
                "user_id": f"{currUser.id}",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            },
            server.JWT_SECRET_KEY,
        )

        return auth_service_pb2.SignInResponse(
            user_id=f"{currUser.id}",
            access_token=accessToken,
        )

    async def SignOut(self, request, context):
        auth_metadata = dict(context.invocation_metadata())

        # # NOTE: We don't need to check if the token is valid here because the
        # # interceptor will do it for us
        auth_header = auth_metadata["authorization"]

        auth_scheme, auth_token = auth_header.split(" ")

        await jwt_blacklist.JWTBlacklist.create(token=auth_token)

        # NOTE: Decrease the number of clients
        await server.server.clientPool.remove(user_id=context.user_id)

        return auth_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
