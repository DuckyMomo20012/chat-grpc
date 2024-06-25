from enum import Enum
from typing import Union

import dearpygui.dearpygui as dpg
import grpc

import pkg.protobuf.auth_service.auth_service_pb2 as auth_service_pb2
import src.client.app as app
from src.shared.pages.base import BasePage
from src.shared.pages.popup import PopupWindow


class AuthMode(Enum):
    SIGN_IN: str = "sign_in"
    SIGN_UP: str = "sign_up"


class AuthPage(BasePage):
    def __init__(self, tag: Union[int, str] = "w_auth"):
        super().__init__(tag)
        self.mode: AuthMode = AuthMode.SIGN_IN

    def nextPage(self):
        from src.client.pages.index import IndexPage

        app.app.goto(IndexPage())

    def switchMode(self, mode: AuthMode):
        self.mode = mode

    def signIn(self, username: str, password: str):
        try:
            response = app.app.client.authServiceStub.SignIn(
                auth_service_pb2.SignInRequest(user_name=username, password=password)
            )

            app.app.userId = response.user_id
            # A little hacky, but less work to do just to get the username
            app.app.userName = username
            app.app.accessToken = response.access_token

            # NOTE: Go to the index page
            self.nextPage()
        except grpc.RpcError as rpc_error:
            dpg.set_value("t_status", rpc_error.details())
            dpg.configure_item("t_status", color=[255, 0, 0])
            dpg.show_item("t_status")

    def signUp(self, username: str, password: str):
        try:
            app.app.client.authServiceStub.SignUp(
                auth_service_pb2.SignUpRequest(user_name=username, password=password)
            )

            PopupWindow(
                "Sign up successful. You can now sign in.",
                label="Notification",
            )
        except grpc.RpcError as rpc_error:
            dpg.set_value("t_status", rpc_error.details())
            dpg.configure_item("t_status", color=[255, 0, 0])
            dpg.show_item("t_status")

    def render(self):
        with dpg.window(label="Sign in", tag=self.tag, width=400, height=200):
            dpg.add_text("Welcome to Chat App!")

            dpg.add_input_text(hint="Username", tag="f_username")
            dpg.add_input_text(hint="Password", tag="f_password", password=True)

            def handleSwitchMode(sender, app_data, user_data):
                if user_data == AuthMode.SIGN_IN:
                    self.switchMode(AuthMode.SIGN_UP)

                    dpg.set_item_label(sender, "Sign in")
                    dpg.set_item_user_data(sender, AuthMode.SIGN_UP)

                    dpg.set_item_label("b_submit", "Sign up")
                    dpg.set_item_user_data("b_submit", AuthMode.SIGN_UP)

                elif user_data == AuthMode.SIGN_UP:
                    self.switchMode(AuthMode.SIGN_IN)

                    dpg.set_item_label(sender, "Sign up")
                    dpg.set_item_user_data(sender, AuthMode.SIGN_IN)

                    dpg.set_item_label("b_submit", "Sign in")
                    dpg.set_item_user_data("b_submit", AuthMode.SIGN_IN)

            # NOTE: A placeholder for the status text
            dpg.add_text("", tag="t_status", show=False)

            with dpg.group(horizontal=True):
                dpg.add_text("Don't have an account?")
                dpg.add_button(
                    label="Sign up",
                    tag="b_switch_mode",
                    callback=handleSwitchMode,
                    user_data=self.mode,
                )

            def handleSubmit(sender, app_data, user_data):
                # NOTE: Hide the status text
                dpg.hide_item("t_status")

                if self.mode == AuthMode.SIGN_IN:
                    self.signIn(
                        dpg.get_value("f_username"), dpg.get_value("f_password")
                    )
                elif self.mode == AuthMode.SIGN_UP:
                    self.signUp(
                        dpg.get_value("f_username"), dpg.get_value("f_password")
                    )

            dpg.add_button(
                label="Sign in",
                tag="b_submit",
                callback=handleSubmit,
                user_data=self.mode,
            )
