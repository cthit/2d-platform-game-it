import pygame


class Renderable():
    def __init__(self, x, y, width, height, sprite=None, draw_function=None, transforms=[]):
        self.sprite = sprite
        self.draw = draw_function
        if draw_function is None:
            self.draw = self._default_draw_function
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.transforms = transforms

    def _default_draw_function(self, screen, pos, size):
        surface = self.sprite
        surface = pygame.transform.scale(surface, size)
        for transform in self.transforms:
            surface = transform(surface)
        screen.blit(surface, pos)
