from typing import Optional, Union

import dearpygui.dearpygui as dpg


class BasePage:
    tag: Union[int, str]

    def __init__(self, tag: Optional[Union[int, str]] = None):
        if tag is None:
            self.tag = dpg.generate_uuid()
        else:
            self.tag = tag

    def __del__(self):
        try:
            # NOTE: Delete the window. This is the important part
            dpg.delete_item(self.tag)
        except SystemError:
            print(
                "RuntimeError: Cannot set primary window. Please check if the window is"
                " created with self.tag"
            )

    def reload(self, isPrimary: bool = True):
        try:
            dpg.delete_item(self.tag)
            self.render()
            if isPrimary:
                dpg.set_primary_window(self.tag, True)
        except SystemError:
            print(
                "RuntimeError: Cannot set primary window. Please check if the window is"
                " created with self.tag"
            )

    def render(self):
        dpg.add_window(label="Base Page", tag=self.tag)
