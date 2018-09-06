import pygame

from src.GameMethods import GameMethods
from src.camera.Camera import Camera
from src.gui.Gui import Gui
from src.gui.elements.text.TextBlock import TextBlock
from src.level import Level
from behaviours import Collide, Collector


class NoLevelFoundException(ValueError):
    pass


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("2d platform game it")
        self.game_methods = GameMethods(self)
        self.screen = pygame.display.set_mode((800, 450))
        self.camera = Camera(self.screen)
        self.isRunning = True
        self.level = None
        self.gui = Gui()
        self.previous_level = None
        self.last_level_coins = 0

    def load_level(self, index):
        try:
            if self.level is not None:
                self.level.clear()

            try:
                self.last_level_coins = self.level.get_entities("Player")[0].get_behaviour(Collector).get_num_collected("Coin")
            except:
                pass

            self.previous_level = self.level
            self.level = Level.get_level_by_index(index)
            if self.level is None:
                raise NoLevelFoundException

            self.level.load()
            self.gui.clear_view()
            try:
                view_name = self.level.config["GUI"]["view"]
                self.gui.load_view(view_name, self.game_methods)
            except KeyError:
                pass
            self.camera.set_settings(self.level.config["Camera"])
            self.camera.set_level(self.level)
            self.time = 0
            self.time_at_last_fps_update = 0
            self.frame_count = 0
        except KeyError:
            pass
        return True

    def restart_level(self):
        self.level.revive_entities()
        for entity in [*self.level.entities]:
            entity.reset()
        self.gui.restart_level()

    def load_next_level(self):
        '''method to change to next level (numberwise)'''
        curr_level = self.level
        self.load_level(-2)
        self.render()
        new_level_num = self.previous_level + 1

        try:
            self.load_level(new_level_num + 1)
        except NoLevelFoundException:
            self.load_level(-1)

    def update(self, delta_time):
        events = pygame.event.get()
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_ESCAPE]:
            self.load_level(0)

        for event in events:
            if event.type == pygame.QUIT:
                self.isRunning = False

        self.gui.update(pygame.mouse, events, delta_time, pressed_keys, self.level.config, self.game_methods)

        for entity in self.level.entities:
            entity.update(delta_time, pressed_keys, self.level.config, self.game_methods)
        pass

    def render(self):
        self.camera.clear()
        bounding_box = self.camera.get_bounding_box()
        self.camera.render_background(self.level.background, bounding_box)
        for renderable in bounding_box.get_visible():
            self.camera.render(renderable, bounding_box)

        self.gui.draw(self.screen)
        pygame.display.update()
