import pygame

from behaviours.Behaviour import Behaviour
from src.GameMethods import GameMethods


class Move(Behaviour):
    def __init__(self, movement_speed = 5, left_key=None, up_key=None, right_key=None, down_key=None):
        self.movement_speed = movement_speed
        self.current_direction = "right"
        self.left_key = left_key
        self.right_key = right_key
        self.up_key = up_key
        self.down_key = down_key

    def update(self, delta_time, keys, config, game_methods: GameMethods):
        if self.left_key is not None and keys[self.left_key]:
            self.move_left()
        elif self.right_key is not None and keys[self.right_key]:
            self.move_right()
        else:
            self.owner.velocity.x *= (0.1 ** delta_time)

        if self.up_key is not None and keys[self.up_key]:
            self.move_up()
        elif self.down_key is not None and keys[self.down_key]:
            self.move_down()

    def move_left(self):
        self.owner.velocity.x = -self.movement_speed
        self.current_direction = "left"

    def move_right(self):
        self.owner.velocity.x = self.movement_speed
        self.current_direction = "right"

    def move_up(self):
        self.owner.velocity.y = -self.movement_speed
        self.current_direction = "up"

    def move_down(self):
        self.owner.velocity.y = self.movement_speed
        self.current_direction = "down"

    def bind_left_to_key(self, keyboard_key):
        self.left_key = keyboard_key

    def bind_right_to_key(self, keyboard_key):
        self.right_key = keyboard_key

    def bind_up_to_key(self, keyboard_key):
        self.up_key = keyboard_key

    def bind_down_to_key(self, keyboard_key):
        self.down_key = keyboard_key

    def set_movement_speed(self, speed: float):
        self.movement_speed = speed