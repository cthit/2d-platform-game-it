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
