import importlib.util
import os

import pygame

from src.GameMethods import GameMethods

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

    def update(self, mouse, events, delta_time, keys, config, game_methods: GameMethods):
        for element in self.gui_elements:
            element.update(mouse, events, delta_time, keys, config, game_methods)

    def clear_view(self):
        self.gui_elements.clear()

    def load_view(self, view_name, game_methods: GameMethods):
        view_loaders[view_name](self, game_methods)

    def add_gui_element(self, gui_element):
        self.gui_elements.append(gui_element)

    def draw(self, screen):
        for element in self.gui_elements:
            element.draw(screen)

    def restart_level(self):
        for element in self.gui_elements:
            element.restart_level()
