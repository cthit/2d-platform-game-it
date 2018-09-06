import pygame

from behaviours.Move import Move
from behaviours.Behaviour import Behaviour
from behaviours.LifeSpan import LifeSpan
from entities.base.Entity import Entity
from src.GameMethods import GameMethods

class Shoot(Behaviour):
    def __init__(self, ammo_class, fire_rate=1, projectile_speed=5, shoot_key=None):
        self.ammo_class = ammo_class
        self.fire_rate = fire_rate
        self.projectile_speed = projectile_speed
        self.shoot_key = shoot_key
        self.cooldown = 0

    def update(self, delta_time, keys, config, game_methods: GameMethods):
        self.cooldown -= delta_time

    def bind_shoot_to_key(self, keyboard_key):
        self.shoot_key = keyboard_key

    def update(self, delta_time, keys, config, game_methods: GameMethods):
        self.cooldown -= delta_time
        if self.shoot_key is not None and keys[self.shoot_key]:
            self.shoot()

    def shoot(self):
        if self.cooldown <= 0:
            self.owner._game_methods.play_sound("shoot-01.wav")
            self.cooldown = 1 / self.fire_rate
            velocity = pygame.Vector2(0, 0)
            x_offset = 0
            if self.owner.has_behaviour(Move):
                move = self.owner.get_behaviour(Move)
                if move.current_direction == "right":
                    velocity = pygame.Vector2(self.projectile_speed, 0)
                    x_offset = 1
                else:
                    velocity = pygame.Vector2(-self.projectile_speed, 0)
                    x_offset = -1

            projectile: Entity = self.owner._game_methods.spawn_entity(
                self.ammo_class,
                self.owner.get_horizontal_center() + x_offset,
                self.owner.get_vertical_center())
            projectile.set_velocity(velocity)
            projectile.register_behaviour(LifeSpan(5))
