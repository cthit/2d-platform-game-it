import importlib.util
import os

import pygame

LEFT = 1

view_loaders = {}


def load_view_loaders():
    for path in [f.path for f in os.scandir("../views") if os.path.splitext(f)[1] == ".py"]:
        view_name = os.path.splitext(os.path.basename(path))[0]
        if ' ' in view_name:
            raise ValueError("Views cannot have spaces in their names, '" + view_name + "'")
        spec = importlib.util.spec_from_file_location("dynamic_load.views." + view_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        view_loaders[view_name] = getattr(module, "load_view")


load_view_loaders()


class Gui:
    def __init__(self):
        self.gui_elements = list()

    def update(self, mouse, events):
        curr_element = None
        for element in self.gui_elements:
            if element.contains(*mouse.get_pos()):
                curr_element = element
                element.on_hover()

        if curr_element is not None:
            for event in events:
                # Check onMouseDown for left mouse button.
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    curr_element.on_mouse_down()
                # Check onMouseUp for left mouse button.
                elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    curr_element.on_mouse_up()

        curr_element = None

    def clear_view(self):
        self.gui_elements.clear()

    def load_view(self, view_name, game):
        view_loaders[view_name](self, game)

    def add_gui_element(self, gui_element):
        self.gui_elements.append(gui_element)

    def draw(self, screen):
        for element in self.gui_elements:
            element.draw(screen)
