import pygame

from src.GameMethods import GameMethods
from src.camera.Camera import Camera
from src.gui.Gui import Gui
from src.gui.elements.text.TextBlock import TextBlock
from src.level import Level
from behaviours import Collide


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

    def load_level(self, index):
        try:
            if self.level is not None:
                self.level.clear()
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
            self.fps_counter = TextBlock("Fps: ", 20, 20)
            self.time_text = TextBlock("T: ", (self.screen.get_rect().width / 2) - 40, 20)
            self.gui.add_gui_element(self.fps_counter)
            self.gui.add_gui_element(self.time_text)
            self.time = 0
            self.time_at_last_text_update = 0
            self.frame_count = 0
        except KeyError:
            pass
        return True

    def reload_entities(self):
        for entity in self.level.entities:
            entity.set_x(entity.spawn_x)
            entity.set_y(entity.spawn_y)
            entity.velocity = pygame.math.Vector2(0, 0)

    def load_next_level(self):
        '''method to change to next level (numberwise)'''
        curr_level = self.level
        self.load_level(-3)
        self.render()
        new_level_num = int(curr_level.config["General"]["index"])

        try:
            self.load_level(new_level_num + 1)
        except NoLevelFoundException:
            self.load_level(-2)

    def update(self, delta_time):
        self.time += delta_time
        self.frame_count += 1

        # Update Fps & clock text
        time_since_last_text_update = self.time - self.time_at_last_text_update
        # Updates 20x/s
        if time_since_last_text_update >= 0.02:
            try:
                fps = int(self.frame_count / time_since_last_text_update)
                time_in_sec = self.time
                milli_seconds = int(time_in_sec * 10)
                seconds = int(time_in_sec % 60)
                time_in_min = (time_in_sec - seconds) / 60
                minutes = int(time_in_min % 60)
                hours = int((time_in_min - minutes) / 60)

                self.fps_counter.update_text("Fps: " + str(fps))
                self.time_text.update_text("LevelTime: " + str(hours) + ":" + str(minutes) + ":" + str(seconds) + ":" + str(milli_seconds))
            except:
                pass
            self.time_at_last_text_update = self.time
            self.frame_count = 0


        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.isRunning = False
        self.gui.update(pygame.mouse, events)

        pressed_keys = pygame.key.get_pressed()

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
