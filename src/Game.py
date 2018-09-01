import pygame

from src.Camera import Camera
from src.LevelData import LevelData
from src.gui.Gui import Gui
from src.gui.elements.image.Image import Image
from src.gui.elements.text.TextBlock import TextBlock
from src.level import Level


class NoLevelFoundException(ValueError):
    pass


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("2d platform game it")
        self.screen = pygame.display.set_mode((800, 450))
        self.camera = Camera(self.screen)
        self.isRunning = True
        self.level = None
        self.state = LevelData(self.load_next_level, self.respawn_player, None)
        self.gui = Gui()

    def load_level(self, index):
        try:
            self.level = Level.get_level_by_index(index)
            if self.level is None:
                raise NoLevelFoundException
            self.level.load()
            self.gui.clear_view()
            try:
                view_name = self.level.config["GUI"]["view"]
                self.gui.load_view(view_name, self)
            except KeyError:
                pass
            self.camera.set_settings(self.level.config["Camera"])
            self.camera.set_level(self.level)
            self.state.level_size = self.level.map_shape
            self.fps_counter = TextBlock("Fps: ", 20, 20)
            self.gui.add_gui_element(self.fps_counter)
        except KeyError:
            pass
        return True

    def respawn_player(self):
        print("Add code to respawn the player.")
        pass

    def load_next_level(self):
        '''method to change to next level (numberwise)'''
        curr_level = self.level
        new_level_num = int(self.level.config["General"]["index"])
        try:
            self.load_level(new_level_num + 1)
        except NoLevelFoundException:
            self.load_level(-2)

    def update(self, delta_time):
        try:
            fps = int(1.0 / delta_time)
            self.fps_counter.update_text("Fps: " + str(fps))
        except:
            pass
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

        self.gui.draw(self.screen)
        pygame.display.update()
