import numpy as np

import pygame

from src.GameMethods import GameMethods
from src.gui.GuiElement import GuiElement
from src.gui.elements.text.TextBlock import TextBlock

pygame.font.init()


class Counter(GuiElement):
    def __init__(self, pos_x, pos_y, value_getter, prefix="", postfix=""):
        super().__init__(pos_x, pos_y, 0, 0)
        self.text_block = TextBlock("", pos_x, pos_y)
        self.value_getter = value_getter
        self.prefix = prefix
        self.postfix = postfix

    def update(self, mouse, events, delta_time, keys, config, game_methods: GameMethods):
        self.text_block.update_text(self.prefix + str(self.value_getter()) + self.postfix)

    def draw(self, surface):
        self.text_block.draw(surface)
