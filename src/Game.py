import pygame

from src.Camera import Camera
from src.level.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("2d platform game it")
        self.screen = pygame.display.set_mode((1600, 900))
        self.camera = Camera(self.screen)
        self.isRunning = True
        self.level = None

    def load_level(self, level_name):
        self.level = Level(level_name)
        self.level.load()
        self.camera.set_settings(self.level.config["Camera"])
        pass

    def update(self, delta_time):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False

        pressed_keys = pygame.key.get_pressed()

        for entity in self.level.entities:
            entity.update(delta_time, pressed_keys, self.level.config)

        pass

    def render(self):
        self.camera.clear()
        for tile in self.level.tiles:
            self.camera.render(tile)
        for entity in self.level.entities:
            self.camera.render(entity)
        pygame.display.update()