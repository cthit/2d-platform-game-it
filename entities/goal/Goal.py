from behaviours.Collide import Collide
from entities.base.Entity import Entity


class Goal(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        self.register_behaviour(Collide())
        self.get_behaviour("Collide").is_trigger = True

    def update(self, deltaTime, keys, config, state):
        super().update(deltaTime, keys, config, state)
        self.goal_reached = state.goal_reached

    def trigger(self, collider):
        if collider.name == "Player":
            if self.goal_reached is None:
                pass
            else:
                self.goal_reached()



