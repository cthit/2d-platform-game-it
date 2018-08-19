import os
import pygame


class Entity:

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../" + name + "/" + name + ".png")
        try:
            self.sprite = pygame.image.load(path)
        except:
            print("Could not load sprite for " + name)

    def update(self, deltaTime, state):
        self.y -= state.gravity * deltaTime;

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
