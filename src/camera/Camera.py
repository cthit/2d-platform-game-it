import pygame
import src.camera.modes.Follow as Follow
import src.camera.modes.Static as Static
import src.camera.modes.Tile as Tile

modes = {
    "Static": Static.get_bounding_box,
    "Follow": Follow.get_bounding_box,
    "Tile": Tile.get_bounding_box
}

class Camera:
    def __init__(self, screen):
        self.screen = screen
        self.level = None
        self.target = None
        self.settings = None

    def set_settings(self, settings):
        self.settings = settings

    def set_level(self, level):
        self.level = level
        self.target = None

    def get_bounding_box(self):
        if self.target is None and "target" in self.settings:
            self.target = self.level.get_entity(self.settings["target"])
        return modes[self.settings["mode"]](self.settings, self.screen, self.level, self.target)

    def render_background(self, background, bounding_box=None):
        #TODO eliassu 2018-09-02, make parallax amount configurable
        parallax_amount = 10
        if background is None:
            return
        if bounding_box is None:
            bounding_box = self.get_bounding_box()
        map_height, map_width = self.level.map_shape
        pos_x = (bounding_box.x_interval[0] + bounding_box.x_interval[1]) / 2
        pos_y = (bounding_box.y_interval[0] + bounding_box.y_interval[1]) / 2

        parallax_scale_factor = (1 + parallax_amount / 100)
        size_x = int(parallax_scale_factor * max(map_width * bounding_box.block_width, self.screen.get_size()[0]))
        size_y = int(parallax_scale_factor * max(map_height * bounding_box.block_height, self.screen.get_size()[1]))
        size = (size_x, size_y)

        parallax_padding_x = size_x - size_x / parallax_scale_factor
        parallax_padding_y = size_y - size_y / parallax_scale_factor

        pos_x = -(pos_x / map_width) * parallax_padding_x * 0.5
        pos_y = -(pos_y / map_height) * parallax_padding_y * 0.5

        sprite = pygame.transform.scale(background, size)
        self.screen.blit(sprite, (pos_x, pos_y))


    # pre-compute and reuse bounding_box for performance gain
    def render(self, renderable, bounding_box=None):
        if bounding_box is None:
            bounding_box = self.get_bounding_box()
        x, _ = bounding_box.x_interval
        y, _ = bounding_box.y_interval

        pos = ((renderable.x - x) * bounding_box.block_width, (renderable.y - y) * bounding_box.block_height)
        size = (int(renderable.width * bounding_box.block_width), int(renderable.height * bounding_box.block_height))
        sprite = pygame.transform.scale(renderable.sprite, size)
        self.screen.blit(sprite, pos)

    def clear(self):
        self.screen.fill((100, 100, 100))
