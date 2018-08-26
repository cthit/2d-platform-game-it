import pygame


class Camera:
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.screen = screen
        self.level = None
        self.target = None
        self.settings = None

    def set_settings(self, settings):
        self.settings = settings

    def set_level(self, level):
        self.level = level
        self.target = None

    def render(self, renderable):
        modes = {
            "Static": self.render_static,
            "Follow": self.render_follow,
            "Tile": self.render_tile
        }
        render_func = modes[self.settings["mode"]]
        block_size = float(self.settings["blocksize"])

        self.x, self.y, block_size_x, block_size_y = render_func(block_size)

        pos = ((renderable.x - self.x) * block_size_x, (renderable.y - self.y) * block_size_y)
        size = (int(renderable.width * block_size_x), int(renderable.height * block_size_y))
        sprite = pygame.transform.scale(renderable.sprite, size)
        self.screen.blit(sprite, pos)

    def render_static(self, block_size):

        x = self.level.get_x(float(self.settings["x"]), self.settings["x-unit"])
        y = self.level.get_y(float(self.settings["y"]), self.settings["y-unit"])

        x -= (self.screen.get_size()[0] / block_size) / 2
        y -= (self.screen.get_size()[1] / block_size) / 2
        return x, y, block_size, block_size

    def render_follow(self, block_size):
        if self.target is None:
            self.target = self.level.get_entity(self.settings["target"])
        x = self.target.get_horizontal_center()
        y = self.target.get_vertical_center()

        x -= (self.screen.get_size()[0] / block_size) / 2
        y -= (self.screen.get_size()[1] / block_size) / 2
        return x, y, block_size, block_size

    def render_tile(self, block_size):
        if self.target is None:
            self.target = self.level.get_entity(self.settings["target"])
        x = self.target.get_horizontal_center()
        y = self.target.get_vertical_center()
        x_offset = float(self.settings["x"])
        y_offset = float(self.settings["y"])
        x_span = float(self.settings["x-span"])
        y_span = float(self.settings["y-span"])
        y += y_offset
        x += x_offset
        x -= (x % x_span) + x_offset
        y -= (y % y_span) + y_offset

        block_size_x = self.screen.get_size()[0] / x_span
        block_size_y = self.screen.get_size()[1] / y_span
        return x, y, block_size_x, block_size_y

    def clear(self):
        self.screen.fill((100, 100, 100))
