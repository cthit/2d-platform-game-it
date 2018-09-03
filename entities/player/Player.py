import pygame

from behaviours.Move import Move
from entities.character.Character import Character


class Player(Character):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        self.register_behaviour(Move(self.movement_speed))

    def update(self, deltaTime, keys, config, state):
        super().update(deltaTime, keys, config, state)

        if state.reload_entities is None:
            pass

        if self.y < -5 or self.y > state.level_size[1] + 5:
            state.reload_entities()