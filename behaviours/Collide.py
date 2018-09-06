from collections import Set
from typing import List

from entities.base.Entity import Entity
from src.utils.QuadTree import Index as QuadTree

from behaviours.Behaviour import Behaviour

quad_tree = QuadTree((-1000, 4000), (-1000, 4000))


def get_top_most_of(collection, default=None):
    if collection is None or len(collection) <= 0:
        return default
    return min(collection, key=lambda i: i.get_top())


def get_bottom_most_of(collection, default=None):
    if collection is None or len(collection) <= 0:
        return default
    return max(collection, key=lambda i: i.get_bottom())


def get_left_most_of(collection, default=None):
    if collection is None or len(collection) <= 0:
        return default
    return min(collection, key=lambda i: i.get_left())


def get_right_most_of(collection, default=None):
    if collection is None or len(collection) <= 0:
        return default
    return max(collection, key=lambda i: i.get_right())


def get_colliding(x_interval, y_interval):
    if x_interval is None or y_interval is None:
        return None
    epsilon = 1e-10
    x_min, x_max = x_interval
    y_min, y_max = y_interval
    x_interval = (x_min - epsilon, x_max + epsilon)
    y_interval = (y_min + epsilon, y_max - epsilon)
    return quad_tree.intersect(x_interval, y_interval)


class Collide(Behaviour):
    def __init__(self, owner=None, is_trigger=False, affects_motion=False):
        self.x_interval = None
        self.y_interval = None
        self.is_trigger = is_trigger
        self.affects_motion = affects_motion
        if owner is None:
            self.owner = None
            return
        else:
            self.set_owner(owner)

    def set_owner(self, new_owner, delta_time, keys, config):
        if new_owner is None:
            return
        owner = self.owner
        if owner is not None:
            owner.remove_listener("set_x", self.update_x_interval)
            owner.remove_listener("set_width", self.update_x_interval)
            owner.remove_listener("set_y", self.update_y_interval)
            owner.remove_listener("set_height", self.update_y_interval)
        self.owner = owner = new_owner
        owner.add_listener("set_x", self.update_x_interval)
        owner.add_listener("set_width", self.update_x_interval)
        owner.add_listener("set_y", self.update_y_interval)
        owner.add_listener("set_height", self.update_y_interval)
        self.update_x_interval()
        self.update_y_interval()

    def update_x_interval(self):
        owner = self.owner
        if owner is None:
            self.x_interval = None
        else:
            self.x_interval = (owner.get_left(), owner.get_right())
            if self.y_interval is not None:
                quad_tree.update_intervals(owner, self.x_interval, self.y_interval)

    def update_y_interval(self):
        owner = self.owner
        if owner is None:
            self.y_interval = None
        else:
            self.y_interval = (owner.get_top(), owner.get_bottom())
            if self.x_interval is not None:
                quad_tree.update_intervals(owner, self.x_interval, self.y_interval)

    def get_other_colliding(self, x_interval, y_interval):
        colliding = get_colliding(x_interval, y_interval)
        to_discard = [self.owner]
        # If the collider is a trigger, ignore it.
        try:
            for collider in colliding:
                if collider.get_behaviour("Collide").is_trigger:
                    collider.trigger(self.owner)
                    to_discard.append(collider)
        except AttributeError:
            pass
        for collider in to_discard:
            colliding.discard(collider)

        return colliding

    def check_inside(self) -> List[Entity]:
        return self.get_other_colliding(self.x_interval, self.y_interval)

    def check_bottom(self, distance=1) -> List[Entity]:
        owner = self.owner
        y_interval = (owner.get_bottom(), owner.get_bottom() + distance)
        return self.get_other_colliding(self.x_interval, y_interval)

    def check_top(self, distance=1) -> List[Entity]:
        owner = self.owner
        y_interval = (owner.get_top() - distance, owner.get_top())
        return self.get_other_colliding(self.x_interval, y_interval)

    def check_left(self, distance=1) -> List[Entity]:
        owner = self.owner
        x_interval = (owner.get_left() - distance, owner.get_left())
        return self.get_other_colliding(x_interval, self.y_interval)

    def check_right(self, distance=1) -> List[Entity]:
        owner = self.owner
        x_interval = (owner.get_right(), owner.get_right() + distance)
        return self.get_other_colliding(x_interval, self.y_interval)

    def check_around(self, distance=1) -> List[Entity]:
        owner = self.owner
        x_interval = (owner.get_left() - distance, owner.get_right() + distance)
        y_interval = (owner.get_top() - distance, owner.get_bottom() + distance)
        return self.get_other_colliding(x_interval, y_interval)

    def clear(self):
        quad_tree.remove(self.owner)

    def __del__(self):
        self.clear()
