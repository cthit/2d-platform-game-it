from behaviours.Behaviour import Behaviour


class Health(Behaviour):
    def __init__(self, hit_points=10, show_health_bar=False):
        self.hit_points = hit_points

    def damage(self, amount):
        self.hit_points -= amount
        if self.hit_points <= 0:
            self.owner.die()

    def render_health_bar(self, screen):
        # TODO show health bar over entity (when hp < max_hp)
        pass

    def heal(self, amount):
        self.hit_points += amount
