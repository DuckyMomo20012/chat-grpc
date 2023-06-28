import asyncio
import logging

import grpc
from tortoise import Tortoise

import pkg.protobuf.auth_service.auth_service_pb2_grpc as auth_service_pb2_grpc
import pkg.protobuf.chat_service.chat_service_pb2_grpc as chat_service_pb2_grpc
import src.server.internal.auth.interceptor.jwt_interceptor as jwt_interceptor
import src.server.internal.auth.services.auth as AuthService
import src.server.internal.chat.services.chat as ChatService
from cli import env

# Coroutines to be invoked when the event loop is shutting down.
_cleanup_coroutines = []


PORT: int = env.int("PORT", 9000)
JWT_SECRET_KEY: str = env.str("JWT_SECRET_KEY")
DB_CONNECTION_STRING: str = env.str("DB_CONNECTION_STRING")


class ClientPool:
    lock: asyncio.Lock
    clients: set[str]

    def __init__(self):
        self.lock = asyncio.Lock()
        self.clients = set()

    async def add(self, user_id: str):
        await self.lock.acquire()

        self.clients.add(user_id)

        self.lock.release()

    async def remove(self, user_id: str):
        await self.lock.acquire()

        self.clients.remove(user_id)

        self.lock.release()


class Server:
    clientPool: ClientPool

    def __init__(self):
        self.clientPool = ClientPool()


async def serve():
    interceptors = [jwt_interceptor.JWTAuthInterceptor(secret_key=JWT_SECRET_KEY)]
    server = grpc.aio.server(interceptors=interceptors)
    chat_service_pb2_grpc.add_ChatServiceServicer_to_server(
        ChatService.ChatService(), server
    )
    auth_service_pb2_grpc.add_AuthServiceServicer_to_server(
        AuthService.AuthService(), server
    )

    listen_addr = f"[::]:{PORT}"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()

    async def server_graceful_shutdown():
        logging.info("Starting graceful shutdown...")
        # Shuts down the server with 5 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(5)

        await Tortoise.close_connections()

    _cleanup_coroutines.append(server_graceful_shutdown())

    # NOTE: Initialize Tortoise ORM
    await Tortoise.init(
        db_url=DB_CONNECTION_STRING,
        modules={
            "models": [
                "src.server.internal.chat.entities.message",
                "src.server.internal.chat.entities.event",
                "src.server.internal.auth.entities.user",
                "src.server.internal.auth.entities.jwt_blacklist",
            ]
        },
    )

    # Generate the schema
    await Tortoise.generate_schemas()

    await server.wait_for_termination()


server = Server()


def main():
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(serve())
    finally:
        loop.run_until_complete(*_cleanup_coroutines)
        loop.close()


if __name__ == "__main__":
    main()
