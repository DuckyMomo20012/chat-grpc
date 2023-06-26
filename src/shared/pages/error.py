import dearpygui.dearpygui as dpg


class ErrorWindow:
    def __init__(self, msg):
        with dpg.window(label="Error"):
            dpg.add_text(msg)
