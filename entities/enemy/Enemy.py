from behaviours.Ai import Ai
from behaviours.Collide import Collide
from behaviours.Fall import Fall
from behaviours.Health import Health
from behaviours.Jump import Jump
from behaviours.KnockBack import KnockBack
from behaviours.Move import Move
from entities.base.Entity import Entity
from src.GameMethods import GameMethods
from behaviours.Shoot import Shoot
from entities.bullet.Bullet import Bullet


class Enemy(Entity):
    def __init__(self, x, y, name):
        Entity.__init__(self, x, y, name)
        self.get_behaviour(Collide).affects_motion = True
        self.movement_speed = 7
        self.register_behaviour(Fall())
        self.register_behaviour(Jump())
        self.register_behaviour(Move())
        self.register_behaviour(KnockBack())
        self.register_behaviour(Health(hit_points=100, show_health_bar=False))
        self.register_behaviour(Shoot(ammo_class=Bullet, fire_rate=2))
        self.register_behaviour(Ai())

    def update(self, delta_time, keys, config, game_methods: GameMethods):
        super().update(delta_time, keys, config, game_methods)
