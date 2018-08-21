import os
import pygame


class Entity:

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.name = name
        self.velocity = pygame.math.Vector2(0, 0)
        self.onFloor = False
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../" + name + "/" + name + ".png")
        try:
            self.sprite = pygame.image.load(path)
        except:
            print("Could not load sprite for " + name)

    def update(self, deltaTime, state):
        if not self.onFloor:
            self.velocity.y = (self.velocity.y + state.gravity * deltaTime)

        self.y = self.y + self.velocity.y
        self.x = self.x + self.velocity.x

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def get_bottom_pos(self):
        return self.y + (self.sprite.get_rect().height / 2)
