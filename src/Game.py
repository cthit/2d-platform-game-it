import pygame

from src.Camera import Camera
from src.LevelData import LevelData
from src.gui.Gui import Gui
from src.level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("2d platform game it")
        self.screen = pygame.display.set_mode((800, 450))
        self.camera = Camera(self.screen)
        self.isRunning = True
        self.level = None
        self.state = LevelData(self.goal_reached)
        self.gui = Gui()

    def load_level(self, index):
        try:
            self.level = Level.get_level_by_index(index)
            self.level.load()
            self.camera.set_settings(self.level.config["Camera"])
            self.camera.set_level(self.level)
        except KeyError:
            pass
        pass

    def goal_reached(self):
        '''method to change to next level (numberwise)'''
        curr_level = self.level
        new_level_num = int(self.level.config["General"]["index"])
        self.load_level(new_level_num + 1)

    def update(self, delta_time):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.isRunning = False
        self.gui.update(pygame.mouse, events)

        pressed_keys = pygame.key.get_pressed()

        for entity in self.level.entities:
            entity.update(delta_time, pressed_keys, self.level.config, self.state)
        pass


    def render(self):
        self.camera.clear()
        for tile in self.level.tiles:
            self.camera.render(tile)
        for entity in self.level.entities:
            self.camera.render(entity)
        pygame.display.update()
