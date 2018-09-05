from behaviours.Behaviour import Behaviour
from src.GameMethods import GameMethods


class Fall(Behaviour):
    def update(self, delta_time, keys, config, game_methods: GameMethods):
        self.owner.velocity.y += float(config["Physics"]["gravity"]) * delta_time;
