from datetime import datetime
from typing import Union

import dearpygui.dearpygui as dpg
import grpc

import pkg.protobuf.chat_service.chat_service_pb2 as chat_service_pb2
import src.client.app as app
from src.shared.pages.base import BasePage
from src.shared.pages.error import ErrorWindow


class IndexPage(BasePage):
    def __init__(self, tag: Union[int, str] = "w_index"):
        super().__init__(tag)
        self.messages = []

        self.fetchMessages()

    def fetchMessages(self):
        try:
            self.messages = app.app.client.chatServiceStub.Fetch(
                chat_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
            )
        except grpc.RpcError:
            ErrorWindow("Cannot fetch messages")

    def render(self):
        with dpg.window(label="Inbox", tag=self.tag, width=400, height=200):
            with dpg.child_window(autosize_x=True, height=-40, border=True):
                for msg in self.messages:
                    with dpg.group(horizontal=True):
                        dpg.add_button(label="i")

                        with dpg.tooltip(dpg.last_item()):
                            parsedTime = datetime.strptime(
                                msg.msg.created_time, "%Y-%m-%d %H:%M:%S.%f%z"
                            ).strftime("%Y-%m-%d %H:%M:%S")

                            dpg.add_text(f"Sent time: {parsedTime}")

                        dpg.add_text(f"{msg.msg.user_name}" + ":")

                        dpg.add_text(f"{msg.msg.content}")

                        dpg.add_button(label="<3")

                        with dpg.popup(
                            dpg.last_item(), mousebutton=dpg.mvMouseButton_Left
                        ):
                            reactionUsers = ", ".join(
                                [reaction.user_name for reaction in msg.msg.reactions]
                            )
                            if not reactionUsers:
                                dpg.add_text("No likes yet")
                            else:
                                dpg.add_text(f"Liked by {reactionUsers}")

                        def handleReact(sender, app_data, user_data):
                            try:
                                app.app.client.chatServiceStub.React(
                                    chat_service_pb2.ReactionRequest(
                                        message_id=user_data["message_id"]
                                    )
                                )

                                dpg.set_item_label(sender, "Liked")
                                dpg.configure_item(sender, enabled=False)
                            except grpc.RpcError:
                                ErrorWindow("User already liked this message")

                        dpg.add_button(
                            label="Like",
                            callback=handleReact,
                            # NOTE: A hack to prevent the late binding problem,
                            # that the message id is always the last message id
                            user_data={"message_id": msg.msg.message_id},
                        )

            with dpg.group(horizontal=True, tag="w_send_message"):
                dpg.add_input_text(hint="Send message...", width=-110)
                dpg.add_button(label="Send", width=100)
