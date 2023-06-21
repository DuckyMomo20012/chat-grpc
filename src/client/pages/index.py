from typing import Union

import dearpygui.dearpygui as dpg

from src.shared.pages.base import BasePage


class IndexPage(BasePage):
    def __init__(self, tag: Union[int, str] = "w_index"):
        super().__init__(tag)

    def render(self):
        msgs = [
            "Welcome to Remote Control!",
            "This is a test message",
            "This is a test message",
            "This is a test message",
            "This is a test message",
            "This is a test message",
            "This is a test message",
            "This is a test message",
            "This is a test message",
            "This is a test message",
            "This is a test message",
            "This is a test message",
        ]

        with dpg.window(label="Inbox", tag=self.tag, width=400, height=200):
            dpg.add_text("Welcome to Remote Control!")

            with dpg.child_window(autosize_x=True, height=-40, border=True):
                for msg in msgs:
                    with dpg.group(horizontal=True):
                        dpg.add_button(label="i")

                        with dpg.tooltip(dpg.last_item()):
                            dpg.add_text("Sent: 2021-10-10 10:10:10")

                        dpg.add_text("DuckyMomo20012" + ":")

                        dpg.add_text(msg)

                        dpg.add_button(label="<3")

                        with dpg.popup(
                            dpg.last_item(), mousebutton=dpg.mvMouseButton_Left
                        ):
                            dpg.add_text("Liked by DuckMomo20012")

                        dpg.add_button(label="Liked")

            with dpg.group(horizontal=True, tag="w_send_message"):
                dpg.add_input_text(hint="Send message...", width=-110)
                dpg.add_button(label="Send", width=100)
