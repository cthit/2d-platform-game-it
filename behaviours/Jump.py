import random

import pygame

from behaviours.Behaviour import Behaviour
from behaviours.Collide import Collide
from src.GameMethods import GameMethods


class Jump(Behaviour):
    def __init__(self, jump_velocity=10, jump_key=None):
        self.jump_velocity = jump_velocity
        self.can_jump = False
        self.jump_key = jump_key
        self._game_methods = None

    def update(self, delta_time, keys, config, game_methods: GameMethods):
        self._game_methods = game_methods
        c = self.owner.get_behaviour(Collide)
        self.can_jump = False
        if len(c.check_bottom(0.05)) > 0:
            if self.owner.velocity.y >= 0:
                self.can_jump = True

        if self.jump_key is not None and keys[self.jump_key]:
            self.jump_if_possible()

    def jump_if_possible(self):
        if self.can_jump:
            self._game_methods.play_sound(random.choice([
                "jump-00.wav",
                "jump-01.wav",
                "jump-02.wav",
                "jump-03.wav"]))
            self.owner.velocity.y = -self.jump_velocity
            self.can_jump = False

    def bind_to_key(self, keyboard_key):
        self.jump_key = keyboard_key
