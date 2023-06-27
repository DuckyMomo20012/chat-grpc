from time import sleep

import dearpygui.dearpygui as dpg


class PopupWindow:
    def __init__(self, msg, label: str, autoClose: bool = True):
        self.tag = dpg.generate_uuid()
        with dpg.window(label=label, tag=self.tag, width=500, height=100):
            dpg.add_text(msg, wrap=500)

        if autoClose:
            self.autoClose()

    def autoClose(self, sec: int = 3):
        counter = 0
        while counter < sec:
            sleep(1)
            counter += 1

        dpg.delete_item(self.tag)
