from typing import Union

import dearpygui.dearpygui as dpg

from src.shared.pages.base import BasePage


class App:
    histories: list[Union[int, str]]

    def __init__(self):
        self.histories = []

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
