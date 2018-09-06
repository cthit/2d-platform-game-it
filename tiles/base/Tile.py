import os
from pathlib import Path

import pygame

from behaviours import Collide
from src.utils.Renderable import Renderable

sprite_map = {}
image_file_formats = [".png", ".jpg", ".jpeg", ".bmp"]

class Tile:
    """A simple tile in the gameworld"""

    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.interval_x = (self.x, self.x + 1)
        self.interval_y = (self.y, self.y + 1)
        Collide.quad_tree.insert(self, self.interval_x, self.interval_y)
        if name in sprite_map:
            self.sprite = sprite_map[name]
        else:
            for format in image_file_formats:
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../" + name.lower() + "/" + name + format)
                if Path(path).is_file():
                    break
            try:
                self.sprite = pygame.image.load(path)
                sprite_map[name] = self.sprite
            except:
                print("Could not load sprite for " + name)
        self.renderable = Renderable(x, y, self.width, self.height, self.sprite)

    def get_renderables(self):
        return [self.renderable]

    def get_top(self):
        return self.y

    def get_vertical_center(self):
        return self.y + self.height / 2

    def get_bottom(self):
        return self.y + self.height

    def get_left(self):
        return self.x

    def get_horizontal_center(self):
        return self.x + self.width / 2

    def get_right(self):
        return self.x + self.width

    def clear(self):
        Collide.quad_tree.remove(self)

    def __del__(self):
        self.clear()
