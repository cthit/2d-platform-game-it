import pygame

from behaviours.Move import Move
from behaviours.Behaviour import Behaviour
from behaviours.LifeSpan import LifeSpan
from entities.base.Entity import Entity
from src.GameMethods import GameMethods


class Shoot(Behaviour):
    def __init__(self, ammo_class, fire_rate=1):
        self.ammo_class = ammo_class
        self.fire_rate = fire_rate
        self.cooldown = 0

    def update(self, delta_time, keys, config, game_methods: GameMethods):
        self.cooldown -= delta_time
        if keys[pygame.K_SPACE] and self.cooldown <= 0:
            game_methods.play_sound("shoot-01.wav")
            self.cooldown = 1 / self.fire_rate
            velocity = pygame.Vector2(0, 0)
            x_offset = 0
            move: Move = self.owner.get_behaviour(Move)
            flip_image = False
            if move is not None:
                if move.current_direction == "right":
                    velocity = pygame.Vector2(5, 0)
                    x_offset = 1
                else:
                    velocity = pygame.Vector2(-5, 0)
                    x_offset = -1

            projectile: Entity = game_methods.spawn_entity(
                self.ammo_class,
                self.owner.get_horizontal_center() + x_offset,
                self.owner.get_vertical_center())
            projectile.set_velocity(velocity)
            projectile.register_behaviour(LifeSpan(5))
            if flip_image:
                projectile.set_width(-projectile.width)
