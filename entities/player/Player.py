import pygame

from behaviours.Move import Move
from entities.character.Character import Character


class Player(Character):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        self.register_behaviour(Move(self.movement_speed))

    def update(self, deltaTime, keys, config):
        super().update(deltaTime, keys, config)


