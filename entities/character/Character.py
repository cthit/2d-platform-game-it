from behaviours.Collide import Collide
from behaviours.Fall import Fall
from behaviours.Jump import Jump
from behaviours.Move import Move
from entities.base.Entity import Entity
from src.GameMethods import GameMethods


class Character(Entity):
    def __init__(self, x, y, name):
        Entity.__init__(self, x, y, name)
        self.movement_speed = 7
        self.register_behaviour(Fall())
        self.register_behaviour(Jump())
        self.get_behaviour(Collide).affects_motion = True
