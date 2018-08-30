import pygame


class Map:
    def __init__(self, level):
        self.open = False
        self.image = pygame.image.load(level.path + "/map.bmp")

    def toggle(self):
        self.open = not self.open

    def draw(self, window):
        if self.open:
            self.image = pygame.transform.scale(self.image, (window.get_width(), window.get_height()))
            window.blit(self.image, (0, 0))