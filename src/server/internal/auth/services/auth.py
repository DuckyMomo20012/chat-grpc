import datetime

import grpc
import jwt
import tortoise.exceptions

import pkg.protobuf.auth_service.auth_service_pb2 as auth_service_pb2
import pkg.protobuf.auth_service.auth_service_pb2_grpc as auth_service_pb2_grpc
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

        # NOTE: Store the client context so we can track the client connection
        # and send messages to the client
        server.server.clients.add(context)

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

    def SignOut(self, request, context):
        try:
            server.server.clients.remove(context)
        except KeyError:
            context.set_details("User is already signed out")
            context.set_code(grpc.StatusCode.NOT_FOUND)

        return auth_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
