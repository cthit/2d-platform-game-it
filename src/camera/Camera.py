import numpy as np

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
            self.target = self.level.get_entities(self.settings["target"])[0]
        return modes[self.settings["mode"]](self.settings, self.screen, self.level, self.target)

    def render_background(self, background, bounding_box=None):
        parallax_amount = 0
        try:
            parallax_amount = float(self.settings['backgroundparallaxamount'])
        except KeyError:
            pass
        if background is None:
            return
        if bounding_box is None:
            bounding_box = self.get_bounding_box()
        screen_size = np.array(self.screen.get_size())

        parallax_scale_factor = (1 + parallax_amount / 100)
        size = parallax_scale_factor * np.array(screen_size)

        bounding_box_center = np.mean((bounding_box.x_interval, bounding_box.y_interval), 1)
        screen_size_in_blocks = screen_size / (bounding_box.block_width, bounding_box.block_height)
        level_size_in_blocks = self.level.map_shape[::-1]
        parallax_padding = size - size / parallax_scale_factor
        pos = -0.5 * (bounding_box_center / np.max((level_size_in_blocks, screen_size_in_blocks))) * parallax_padding

        sprite = pygame.transform.scale(background, size.astype(int))
        self.screen.blit(sprite, pos)


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
