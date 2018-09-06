from behaviours.Collide import Collide
from entities.base.Entity import Entity
from src.GameMethods import GameMethods


class Goal(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        self.register_behaviour(Collide())
        self.get_behaviour("Collide").is_trigger = True
        self.go_to_next_level = None

    def update(self, deltaTime, keys, config, game_methods: GameMethods):
        super().update(deltaTime, keys, config, game_methods)
        self.go_to_next_level = game_methods.load_level_complete()

    def trigger(self, collider):
        if collider.name == "Player":
            if self.go_to_next_level is None:
                pass
            else:
                self.go_to_next_level()



