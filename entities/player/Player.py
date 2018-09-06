import pygame

from behaviours.Collector import Collector
from behaviours.Jump import Jump
from behaviours.Move import Move
from behaviours.Shoot import Shoot
from behaviours.Health import Health
from entities.bullet.Bullet import Bullet
from entities.character.Character import Character
from src.GameMethods import GameMethods


class Player(Character):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        move = self.register_behaviour(Move(self.movement_speed))
        self.register_behaviour(Shoot(ammo_class=Bullet, fire_rate=10))

        self.register_behaviour(Collector())
        self.register_behaviour(Health(hit_points=50, show_health_bar=False))

        self.get_behaviour(Jump).bind_to_key(pygame.K_w)
        move.set_movement_speed(7)
        move.bind_left_to_key(pygame.K_a)
        move.bind_right_to_key(pygame.K_d)

    def update(self, deltaTime, keys, config, game_methods: GameMethods):
        super().update(deltaTime, keys, config, game_methods)

        if self.y < -5 or self.y > game_methods.get_level_dimensions()[1] + 5:
            game_methods.restart_level()

        if keys[pygame.K_SPACE]:
            self.get_behaviour(Shoot).shoot(deltaTime, keys, config, game_methods)

    def die(self):
        super().die()
        self._game_methods.restart_level()
