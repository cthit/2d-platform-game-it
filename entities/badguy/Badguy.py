import pygame

from entities.character.Character import Character
from src.GameMethods import GameMethods


class Badguy(Character):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)

    def update(self, deltaTime, keys, config, game_methods: GameMethods):
        super().update(deltaTime, keys, config, game_methods)