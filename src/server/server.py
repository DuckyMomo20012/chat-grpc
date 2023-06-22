import asyncio
import logging

import grpc

import pkg.protobuf.chat_service.chat_service_pb2_grpc as chat_service_pb2_grpc
from src.server.internal.chat.services.chat import ChatService

# Coroutines to be invoked when the event loop is shutting down.
_cleanup_coroutines = []


async def serve():
    server = grpc.aio.server()
    chat_service_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    listen_addr = "[::]:9000"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()

    async def server_graceful_shutdown():
        logging.info("Starting graceful shutdown...")
        # Shuts down the server with 5 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(5)

    _cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()


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
