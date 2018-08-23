from behaviours.Behaviour import Behaviour


class Fall(Behaviour):
    def update(self, owner, delta_time, keys, config):
        owner.velocity.y += float(config["Physics"]["gravity"]) * delta_time;
