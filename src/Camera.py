import pygame


class Camera:
    def __init__(self, screen):
        self.x = -40
        self.y = -20
        self.screen = screen

    def set_center(self, x, y):
        self.x = x
        self.y = y

    def set_settings(self, settings):
        self.settings = settings

    def render(self, renderable):
        block_size = float(self.settings["blocksize"])
        pos = ((renderable.x - self.x) * block_size, (renderable.y - self.y) * block_size)
        size = (int(renderable.width * block_size), int(renderable.height * block_size))
        sprite = pygame.transform.scale(renderable.sprite, size)
        self.screen.blit(sprite, pos)

    def clear(self):
        self.screen.fill((100, 100, 100))