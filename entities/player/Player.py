import pygame

from behaviours.Move import Move
from entities.character.Character import Character
from src.GameMethods import GameMethods


class Player(Character):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        self.register_behaviour(Move(self.movement_speed))

    def update(self, deltaTime, keys, config, game_methods: GameMethods):
        super().update(deltaTime, keys, config, game_methods)

        if self.y < -5 or self.y > game_methods.get_level_dimensions()[1] + 5:
            game_methods.restart_level()
