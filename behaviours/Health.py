import pygame

from behaviours.Behaviour import Behaviour
from entities.base.Entity import Entity
from src.utils.Renderable import Renderable

_BAR_HEIGHT = 0.1


class Health(Behaviour):
    def __init__(self, hit_points=10, max_hit_points=10, show_health_bar=False):
        self.initial_hit_points = hit_points
        self.max_hit_points = max_hit_points
        self.hit_points = hit_points
        self.show_health_bar = show_health_bar
        self.health_bar = None


    def damage(self, amount):
        self.hit_points -= amount
        if self.hit_points <= 0:
            self.owner.die()

    def heal(self, amount):
        self.hit_points += amount

    def get_renderables(self):
        if not self.show_health_bar:
            return []
        if self.health_bar is None:
            self.health_bar = HealthBar(self.owner, self)
        return [self.health_bar.as_renderable()]

    def reset(self):
        self.hit_points = self.initial_hit_points


class HealthBar():
    def __init__(self, owner: Entity, health: Health):
        self.owner = owner
        self.health = health

    def as_renderable(self):
        o = self.owner
        return Renderable(o.x, o.y - 0.25, o.width, _BAR_HEIGHT, draw_function=self.draw)

    def draw(self, screen: pygame.Surface, pos, size):

        damage_ratio = self.health.hit_points / self.health.max_hit_points
        if damage_ratio >= 1:
            return

        x_min = pos[0]
        x_max = pos[0] + size[0]
        x_hp = x_min + (x_max - x_min) * damage_ratio

        pygame.draw.line(
            screen,
            (255, 0, 0),  # RED
            (x_hp, pos[1]),
            (x_max, pos[1]),
            int(size[1])
        )

        pygame.draw.line(
            screen,
            (0, 255, 0),  # GREEN
            (x_min, pos[1]),
            (x_hp, pos[1]),
            int(size[1])
        )
