import pygame

from behaviours.Behaviour import Behaviour
from behaviours.Collide import Collide


class Jump(Behaviour):
    def __init__(self, jump_velocity=10):
        self.jump_velocity = jump_velocity
        self.can_jump = False

    def update(self, owner, delta_time, keys, config):
        c = owner.get_behaviour(Collide)
        if len(c.check_bottom(0.05)) > 0:
            self.can_jump = True
        if self.can_jump and keys[pygame.K_w]:
            owner.velocity.y = -self.jump_velocity
            self.can_jump = False
