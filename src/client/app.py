import asyncio
import logging
from typing import Union

import dearpygui.dearpygui as dpg
import grpc

import pkg.protobuf.chat_service.chat_service_pb2_grpc as chat_service_pb2_grpc
from src.shared.pages.base import BasePage


class Client:
    chatServiceStub: chat_service_pb2_grpc.ChatServiceStub

    def __init__(self):
        self.chatServiceStub = None

        asyncio.run(self.connect())

    async def connect(self):
        async with grpc.aio.insecure_channel("localhost:9000") as channel:
            self.chatServiceStub = chat_service_pb2_grpc.ChatServiceStub(channel)


class App:
    histories: list[Union[int, str]]
    client: Client

    def __init__(self):
        self.histories = []

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
    from src.client.pages.index import IndexPage

    logging.basicConfig()

    dpg.create_context()
    dpg.create_viewport(title="Chat App", width=800, height=600)

    with dpg.font_registry():
        # First argument ids the path to the .ttf or .otf file
        with dpg.font("assets/fonts/IBMPlexMono-Regular.ttf", 20) as default_font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Vietnamese)

    dpg.bind_font(default_font)

    app.goto(IndexPage())

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
