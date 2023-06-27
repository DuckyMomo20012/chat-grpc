from datetime import datetime
from typing import Union

import dearpygui.dearpygui as dpg
import grpc

import pkg.protobuf.auth_service.auth_service_pb2 as auth_service_pb2
import pkg.protobuf.chat_service.chat_service_pb2 as chat_service_pb2
import src.client.app as app
import src.client.listener.event as eventListener
from src.shared.pages.base import BasePage
from src.shared.pages.error import ErrorWindow


def handleEventListener(page: BasePage, event: chat_service_pb2.SubscribeResponse):
    if event.type == "EventType.MESSAGE":
        page.refresh()

    elif event.type == "EventType.REACTION":
        pass
    else:
        # Event type is unknown, so we just refresh the page
        page.refresh()

    # NOTE: Send back the last event id to the server, so the server
    # acknowledges that we have received the event, and the server will
    # delete the event from the queue
    return chat_service_pb2.SubscribeRequest(event_id=event.event_id)


class IndexPage(BasePage):
    def __init__(self, tag: Union[int, str] = "w_index"):
        super().__init__(tag)
        self.messages = []

        self.fetchMessages()

        # NOTE: Add event listener
        self.listener = eventListener.EventListener()
        self.listener.addEventListener(self, handleEventListener)

    def refresh(self):
        self.fetchMessages()
        self.reload()

    def signOut(self):
        try:
            app.app.client.authServiceStub.SignOut(
                auth_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
            )
            app.app.accessToken = None
            app.app.back()
        except grpc.RpcError:
            ErrorWindow("Cannot sign out")

    def fetchMessages(self):
        try:
            self.messages = app.app.client.chatServiceStub.Fetch(
                chat_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
            )
        except grpc.RpcError:
            ErrorWindow("Cannot fetch messages")

    def render(self):
        with dpg.window(label="Inbox", tag=self.tag, width=400, height=200):
            with dpg.menu_bar():
                dpg.add_menu_item(label="Refresh", callback=self.refresh)
                dpg.add_menu_item(label="Sign out", callback=self.signOut)

            with dpg.child_window(
                tag="w_inbox", autosize_x=True, height=-40, border=True
            ):
                for msg in self.messages:
                    with dpg.group(horizontal=True):
                        dpg.add_button(label="i")

                        with dpg.tooltip(dpg.last_item()):
                            parsedTime = datetime.strptime(
                                msg.msg.created_time, "%Y-%m-%d %H:%M:%S.%f%z"
                            ).strftime("%Y-%m-%d %H:%M:%S")

                            dpg.add_text(f"Sent time: {parsedTime}")

                        dpg.add_text(f"{msg.msg.user_name}" + ":")

                        if msg.msg.user_id == app.app.userId:
                            dpg.configure_item(dpg.last_item(), color=(0, 255, 0))

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

                        isReacted = any(
                            reaction.user_id == app.app.userId
                            for reaction in msg.msg.reactions
                        )

                        dpg.add_button(
                            label="Like" if not isReacted else "Liked",
                            enabled=not isReacted,
                            callback=handleReact,
                            # NOTE: A hack to prevent the late binding problem,
                            # that the message id is always the last message id
                            user_data={"message_id": msg.msg.message_id},
                        )

            # NOTE: Scroll to the bottom
            dpg.set_y_scroll("w_inbox", -1)

            with dpg.group(horizontal=True):
                dpg.add_input_text(
                    hint="Send message...", tag="f_send_message", width=-110
                )

                def handleSend(sender, app_data, user_data):
                    try:
                        messageContent = dpg.get_value("f_send_message")

                        if not messageContent:
                            raise ValueError("Message cannot be empty")

                        app.app.client.chatServiceStub.Send(
                            chat_service_pb2.SendRequest(
                                content=messageContent,
                            )
                        )

                        # NOTE: DO NOT refresh the page here, because the event
                        # listener will do it for us
                        # self.refresh()
                    except grpc.RpcError:
                        ErrorWindow("Cannot send message")
                    except ValueError as e:
                        ErrorWindow(str(e))

                dpg.add_button(label="Send", callback=handleSend, width=100)
