from entities.base.Entity import Entity
import pygame

class Character(Entity):

    def __init__(self, x, y, name, movement_speed = 10):
        Entity.__init__(self, x, y, name)
        self.movementSpeed = movement_speed
        self.velocity = pygame.math.Vector2(0, 0)
        self.onFloor = False

    def update(self, deltaTime, state):
        if not self.onFloor:
            self.velocity.y = (self.velocity.y + state.gravity * deltaTime)

        self.y = self.y + self.velocity.y
        self.x = self.x + self.velocity.x