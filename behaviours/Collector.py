from behaviours.Collectible import Collectible
from behaviours.Behaviour import Behaviour
from src.GameMethods import GameMethods


class Collector(Behaviour):
    def __init__(self):
        self.collected = {}

    def collect(self, collectible):
        name = collectible.name
        collection_sound = collectible.get_behaviour(Collectible).collection_sound
        # game_methods.play_sound(collection_sound)
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
