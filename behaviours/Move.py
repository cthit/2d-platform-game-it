import pygame

from behaviours.Behaviour import Behaviour


class Move(Behaviour):
    def __init__(self, movement_speed = 5, key_map=None):
        if key_map is None:
            key_map = {"left": pygame.K_a, "right": pygame.K_d}
        self.key_map = key_map
        self.movement_speed = movement_speed

    def update(self, owner, delta_time, keys, config):
        if keys[self.key_map["left"]]:
            owner.velocity.x = -self.movement_speed
        elif keys[self.key_map["right"]]:
            owner.velocity.x = self.movement_speed
        else:
            owner.velocity.x = 0