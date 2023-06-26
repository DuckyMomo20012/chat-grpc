from typing import Optional, Union

import dearpygui.dearpygui as dpg


class BasePage:
    tag: Union[int, str]

    def __init__(self, tag: Optional[Union[int, str]] = None):
        if tag is None:
            self.tag = dpg.generate_uuid()
        else:
            self.tag = tag

    def reload(self, isPrimary: bool = True):
        dpg.delete_item(self.tag)
        self.render()
        if isPrimary:
            dpg.set_primary_window(self.tag, True)

    def render(self):
        dpg.add_window(label="Base Page", tag=self.tag)
