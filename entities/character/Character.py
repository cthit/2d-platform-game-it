from behaviours.Collide import Collide
from behaviours.Fall import Fall
from behaviours.Jump import Jump
from behaviours.Move import Move
from entities.base.Entity import Entity

class Character(Entity):
    def __init__(self, x, y, name):
        Entity.__init__(self, x, y, name)
        self.movement_speed = 7
        self.register_behaviour(Collide())
        self.register_behaviour(Fall())
        self.register_behaviour(Jump())

    def update(self, delta_time, keys, config, state):
        super().update(delta_time, keys, config, state)
