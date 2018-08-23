import pygame

from entities.character.Character import Character


class Player(Character):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)

    def update(self, deltaTime, state):
        if state.keys[pygame.K_a]:
            self.velocity.x = -self.movementSpeed
        if state.keys[pygame.K_d]:
            self.velocity.x = self.movementSpeed

        super().update(deltaTime, state)


