import os

import pygame

class Tile:
    """A simple tile in the gameworld"""

    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../" + name + "/" + name + ".png")
        try:
            self.sprite = pygame.image.load(path)
        except:
            print("Could not load sprite for " + name)

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def get_top_position(self):
        return self.x - (self.sprite.get_rect().height / 2)