class Behaviour:
    def __init__(self, owner=None):
        from entities.base.Entity import Entity
        self.owner: Entity = owner

    def set_owner(self, new_owner, delta_time, keys, config):
        self.owner = new_owner

    def update(self, delta_time, keys, config, game_methods):
        pass

    def get_renderables(self):
        return []
