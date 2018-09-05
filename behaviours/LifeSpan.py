from behaviours.Behaviour import Behaviour
from src.GameMethods import GameMethods


class LifeSpan(Behaviour):
    def __init__(self, seconds=10):
        self.remaining_time = seconds

    def update(self, delta_time, keys, config, game_methods: GameMethods):
        self.remaining_time -= delta_time
        if self.remaining_time <= 0:
            game_methods.kill_entity(self.owner)
