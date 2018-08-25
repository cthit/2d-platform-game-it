import pygame

from src.Camera import Camera
from src.LevelData import LevelData
from src.level.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("2d platform game it")
        self.screen = pygame.display.set_mode((1600, 900))
        self.camera = Camera(self.screen)
        self.isRunning = True
        self.level = None
        self.state = LevelData(self.goal_reached)

    def load_level(self, level_name):
        try:
            self.level = Level(level_name)
            self.level.load()
            self.camera.set_settings(self.level.config["Camera"])
        except KeyError:
            pass
        pass

    def goal_reached(self):
        '''method to change to next level (numberwise)'''
        curr_level = self.level.name
        level_num = ""

        if len(curr_level) <= 0:
            print("Current level has no name?")
            return

        class BreakIt(Exception): pass

        try:
            for character in curr_level.split()[::-1]:
                if character.isdigit():
                    level_num += character
                else:
                    raise BreakIt
        except BreakIt:
            pass

        level_num = level_num[::-1]
        level_num = int(level_num)
        level_num += 1
        self.load_level("level" + str(level_num))

    def update(self, delta_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False

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