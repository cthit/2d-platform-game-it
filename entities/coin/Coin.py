from behaviours.Collectible import Collectible
from entities.base.Entity import Entity


class Coin(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        self.register_behaviour(Collectible(collection_sound="pickup-01.wav"))


