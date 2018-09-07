from entities.trigger_base.Trigger import Trigger
from src.GameMethods import GameMethods


class Goal(Trigger):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        self.go_to_next_level = None

    def update(self, delta_time, keys, config, game_methods: GameMethods):
        super().update(delta_time, keys, config, game_methods)
        self.go_to_next_level = game_methods.load_level_complete

    def on_collide(self, colliding_objects, delta_time, keys, config, game_methods: GameMethods):
        for collider in colliding_objects:
            if collider.name == "Player":
                if self.go_to_next_level is None:
                    pass
                else:
                    self.go_to_next_level()



