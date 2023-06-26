import logging
from typing import Union

import dearpygui.dearpygui as dpg
import grpc

import pkg.protobuf.auth_service.auth_service_pb2_grpc as auth_service_pb2_grpc
import pkg.protobuf.chat_service.chat_service_pb2_grpc as chat_service_pb2_grpc
import src.client.interceptor.token_interceptor as token_interceptor
from cli import env
from src.shared.pages.base import BasePage

PORT: int = env.int("PORT", 9000)
SERVER_HOST: str = env.str("SERVER_HOST", "localhost")


class Client:
    channel: grpc.Channel
    authServiceStub: auth_service_pb2_grpc.AuthServiceStub
    chatServiceStub: chat_service_pb2_grpc.ChatServiceStub

    def __init__(self):
        self.channel = None
        self.userServiceStub = None
        self.chatServiceStub = None

        self.connect()

    def __del__(self):
        self.channel.close()

    def connect(self):
        interceptors = [token_interceptor.TokenInterceptor()]

        self.channel = grpc.insecure_channel(f"{SERVER_HOST}:{PORT}")

        self.channel = grpc.intercept_channel(self.channel, *interceptors)

        self.authServiceStub = auth_service_pb2_grpc.AuthServiceStub(self.channel)
        self.chatServiceStub = chat_service_pb2_grpc.ChatServiceStub(self.channel)


class App:
    histories: list[Union[int, str]]
    userId: str
    accessToken: str
    client: Client

    def __init__(self):
        self.histories = []
        self.userId = None
        self.accessToken = None
        self.client = Client()

    def goto(self, page: BasePage):
        if len(self.histories) > 0:
            dpg.configure_item(self.histories[-1], show=False)
        page.render()
        # NOTE: Tag can be re-assigned while rendering
        self.histories.append(page.tag)

        dpg.set_primary_window(page.tag, True)

    def back(self):
        if len(self.histories) > 1:
            prevPage = self.histories.pop()
            dpg.delete_item(prevPage)
            dpg.configure_item(self.histories[-1], show=True)


app = App()


def main():
    from src.client.pages.auth import AuthPage

    logging.basicConfig()

    dpg.create_context()
    dpg.create_viewport(title="Chat App", width=800, height=600)

    with dpg.font_registry():
        # First argument ids the path to the .ttf or .otf file
        with dpg.font("assets/fonts/IBMPlexMono-Regular.ttf", 20) as default_font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Vietnamese)

    dpg.bind_font(default_font)

    app.goto(AuthPage())

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
