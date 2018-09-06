import pygame


class Renderable():
    def __init__(self, x, y, width, height, sprite=None, draw_function=None):
        self.sprite = sprite
        self.draw = draw_function
        if draw_function is None:
            self.draw = self._default_draw_function
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def _default_draw_function(self, screen, pos, size):
        screen.blit(pygame.transform.scale(self.sprite, size), pos)
