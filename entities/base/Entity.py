import os
import pygame


class Entity:

    def __init__(self, x, y, name):
        self.spawnX = x
        self.spawnY = y
        self.name = name
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../" + name + "/" + name + ".png")
        self.sprite = pygame.image.load(path)

    def update(self, deltaTime, state):
        self.y -= state.gravity * deltaTime;

