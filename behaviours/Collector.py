from behaviours.Collectible import Collectible
from behaviours.Collide import Collide
from behaviours.Behaviour import Behaviour
from src.GameMethods import GameMethods
from tiles.base.Tile import Tile


class Collector(Behaviour):
    def __init__(self):
        self.collected = {}

    def update(self, delta_time, keys, config, game_methods: GameMethods):
        c = self.owner.get_behaviour(Collide)
        for collectible in [x for x in c.check_around(0.1) if not isinstance(x, Tile) and x.get_behaviour(Collectible) is not None]:
            name = collectible.name
            collection_sound = collectible.get_behaviour(Collectible).collection_sound
            game_methods.play_sound(collection_sound)
            if name in self.collected:
                self.collected[name] += 1
            else:
                self.collected[name] = 1
            collectible.die()

    def get_num_collected(self, collectible_name):
        if collectible_name in self.collected:
            return self.collected[collectible_name]
        else:
            return 0

    def reset(self):
        self.collected = {}
