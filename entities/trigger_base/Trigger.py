from behaviours.Collectible import Collectible
from behaviours.Collector import Collector
from entities.base.Entity import Entity
from src.GameMethods import GameMethods


class Trigger(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        self.get_behaviour("Collide").is_trigger = True

    def on_collide_bottom(self, colliding_objects, delta_time, keys, config, game_methods: GameMethods):
        return

    def on_collide_top(self, colliding_objects, delta_time, keys, config, game_methods: GameMethods):
        return

    def on_collide_left(self, colliding_objects, delta_time, keys, config, game_methods: GameMethods):
        return

    def on_collide_right(self, colliding_objects, delta_time, keys, config, game_methods: GameMethods):
        return

    def trigger(self, collider: Entity):
        if self.has_behaviour(Collectible):
            if collider.has_behaviour(Collector):
                collector = collider.get_behaviour(Collector)
                collector.collect(self)

