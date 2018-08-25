import os

import pygame
from intervaltree import Interval

from behaviours import Collide


class Tile:
    """A simple tile in the gameworld"""

    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.interval_x = Interval(self.x, self.x + 1, self)
        self.interval_y = Interval(self.y, self.y + 1, self)
        Collide.tx.add(self.interval_x)
        Collide.ty.add(self.interval_y)

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../" + name.lower() + "/" + name + ".png")
        try:
            self.sprite = pygame.image.load(path)
        except:
            print("Could not load sprite for " + name)

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

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

    def __del__(self):
        Collide.tx.discard(self.interval_x)
        Collide.ty.discard(self.interval_y)
