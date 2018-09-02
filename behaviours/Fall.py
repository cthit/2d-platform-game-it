from behaviours.Behaviour import Behaviour


class Fall(Behaviour):
    def update(self, delta_time, keys, config):
        self.owner.velocity.y += float(config["Physics"]["gravity"]) * delta_time;
