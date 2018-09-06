from behaviours.Ai import Ai
from behaviours.Collide import Collide
from behaviours.Fall import Fall
from behaviours.Health import Health
from behaviours.Jump import Jump
from behaviours.KnockBack import KnockBack
from behaviours.Move import Move
from behaviours.Shoot import Shoot
from entities.base.Entity import Entity
from entities.bullet.Bullet import Bullet
from src.GameMethods import GameMethods
from behaviours.Shoot import Shoot
from entities.bullet.Bullet import Bullet
from tiles.base.Tile import Tile


class Enemy(Entity):
    def __init__(self, x, y, name):
        Entity.__init__(self, x, y, name)
        self.get_behaviour(Collide).affects_motion = True
        self.movement_speed = 7
        self.damage = 10
        self.cooldown = 0
        self.damageRate = 2
        self.register_behaviour(Fall())
        self.register_behaviour(Jump())
        self.register_behaviour(Move())
        self.register_behaviour(KnockBack())
        self.register_behaviour(Health(hit_points=100, max_hit_points=100, show_health_bar=True))
        self.register_behaviour(Shoot(ammo_class=Bullet, fire_rate=2))
        self.register_behaviour(Ai())

    def update(self, delta_time, keys, config, game_methods: GameMethods):
        super().update(delta_time, keys, config, game_methods)
        self.cooldown -= delta_time
        if self.cooldown <= 0:
            self.cooldown = 1 / self.damageRate
            c = self.get_behaviour(Collide)
            for colliding in c.check_around(0.001):
                if isinstance(colliding, Tile):
                    return
                health: Health = colliding.get_behaviour(Health)
                knock_back: KnockBack = colliding.get_behaviour(KnockBack)
                if knock_back is not None:
                    knock_back.push(self.velocity, self.mass)
                if health is not None:
                    health.damage(self.damage)
