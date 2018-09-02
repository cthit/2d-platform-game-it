from intervaltree import Interval

from behaviours import Collide


class BoundingBox:
    def __init__(self, x_interval, y_interval, block_width, block_height):
        self.x_interval = x_interval
        self.y_interval = y_interval
        self.block_height = block_height
        self.block_width = block_width

    def get_visible(self, padding=2):
        x_min, x_max = self.x_interval
        x_min -= padding
        x_max += padding
        y_min, y_max = self.y_interval
        y_min -= padding
        y_max += padding
        return Collide.get_colliding(Interval(x_min, x_max), Interval(y_min, y_max))
