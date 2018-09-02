class Behaviour:
    def __init__(self, owner=None):
        self.owner = owner

    def set_owner(self, new_owner, delta_time, keys, config):
        self.owner = new_owner

    def update(self, delta_time, keys, config):
        pass