from threading import Thread
from typing import Callable, Optional

import pkg.protobuf.chat_service.chat_service_pb2 as chat_service_pb2
import src.client.app as app
from src.shared.pages.base import BasePage


# NOTE: Just a name for listener that subscribes to events, not a real event
# listener implementation
class EventListener:
    exitFlag: bool
    thread: Thread

    def __init__(self):
        self.exitFlag = False
        self.thread = None

    def __del__(self):
        self.stop()

    def addEventListener(
        self,
        page: BasePage,
        callback: Callable[
            [chat_service_pb2.SubscribeResponse],
            Optional[chat_service_pb2.SubscribeRequest],
        ],
    ):
        def _loop():
            newRequest: chat_service_pb2.SubscribeRequest = None
            while not self.exitFlag:
                if not newRequest:
                    events = app.app.client.chatServiceStub.Subscribe(
                        chat_service_pb2.SubscribeRequest()
                    )
                else:
                    # NOTE: We have to send back the last event id to the
                    # server, to delete the event from the queue
                    events = app.app.client.chatServiceStub.Subscribe(newRequest)

                    # NOTE: Reset the new request so that we don't send the
                    # stale event id to the server
                    newRequest = None

                # NOTE: Loop through event queue
                for event in events:
                    newRequest = callback(page, event)

        self.thread = Thread(target=_loop)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        self.exitFlag = True
        self.thread.join()
