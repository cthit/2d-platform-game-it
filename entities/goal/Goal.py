from behaviours.Collide import Collide
from entities.base.Entity import Entity


class Goal(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        self.register_behaviour(Collide())
        self.get_behaviour("Collide").is_trigger = True
