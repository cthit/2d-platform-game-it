from behaviours.Behaviour import Behaviour


class Collectible(Behaviour):
    def __init__(self, collection_sound: str=None):
        self.collection_sound = collection_sound
