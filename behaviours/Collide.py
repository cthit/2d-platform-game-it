from typing import Set

from intervaltree import Interval, IntervalTree

from behaviours.Behaviour import Behaviour

tx = IntervalTree()
ty = IntervalTree()


def get_overlapping_x_data(x_interval):
    if x_interval is None:
        return None
    return set([i.data for i in tx[x_interval.begin:x_interval.end]])


def get_overlapping_y_data(y_interval):
    if y_interval is None:
        return None
    return set([i.data for i in ty[y_interval.begin:y_interval.end]])


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


def get_right_most_of(collection,default=None):
    if collection is None or len(collection) <= 0:
        return default
    return max(collection, key=lambda i: i.get_right())


def get_colliding(x_interval, y_interval):
    if x_interval is None or y_interval is None:
        return None
    x_overlaps = get_overlapping_x_data(x_interval)
    y_overlaps = get_overlapping_y_data(y_interval)
    return x_overlaps.intersection(y_overlaps)


class Collide(Behaviour):
    def __init__(self, owner=None, is_trigger = False):
        self.x_interval = None
        self.y_interval = None
        self.is_trigger = is_trigger
        if owner is None:
            self.owner = None
            return
        else:
            self.set_owner(owner)

    def set_owner(self, new_owner, delta_time, keys, config):
        if new_owner is None:
            return
        owner = self.owner
        if not owner is None:
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
        tx.discard(self.x_interval)
        if owner is None:
            self.x_interval = None
        else:
            self.x_interval = Interval(owner.get_left(), owner.get_right(), owner)
        tx.add(self.x_interval)

    def update_y_interval(self):
        owner = self.owner
        ty.discard(self.y_interval)
        if owner is None:
            self.y_interval = None
        else:
            self.y_interval = Interval(owner.get_top(), owner.get_bottom(), owner)
        ty.add(self.y_interval)

    # The collision behaviour is only intended to add functionality
    # that can be utilized by other behaviours of an entity.
    # The update function should not do anything here
    def update(self, new_owner, delta_time, keys, config):
        pass

    def get_other_colliding(self, x_interval, y_interval):
        colliding = get_colliding(x_interval, y_interval)
        to_discard = [self.owner]
        # If the collider is a trigger, ignore it.
        try:
            for collider in colliding:
                if collider.get_behaviour("Collide").is_trigger:
                    to_discard.append(collider)
        except AttributeError:
            pass
        for collider in to_discard:
            colliding.discard(collider)

        return colliding

    def check_inside(self):
        owner = self.owner
        return self.get_other_colliding(self.x_interval, self.y_interval)

    def check_bottom(self, distance=1):
        owner = self.owner
        y_interval = Interval(owner.get_bottom(), owner.get_bottom() + distance)
        return self.get_other_colliding(self.x_interval, y_interval)

    def check_top(self, distance=1):
        owner = self.owner
        y_interval = Interval(owner.get_top() - distance, owner.get_top())
        return self.get_other_colliding(self.x_interval, y_interval)

    def check_left(self, distance=1):
        owner = self.owner
        x_interval = Interval(owner.get_left() - distance, owner.get_left())
        return self.get_other_colliding(x_interval, self.y_interval)

    def check_right(self, distance=1):
        owner = self.owner
        x_interval = Interval(owner.get_right(), owner.get_right() + distance)
        return self.get_other_colliding(x_interval, self.y_interval)

    def __del__(self):
        try:
            if self.x_inteval is not None:
                tx.remove(self.x_interval)
            if self.y_inteval is not None:
                ty.remove(self.y_interval)
        except AttributeError:
            pass
