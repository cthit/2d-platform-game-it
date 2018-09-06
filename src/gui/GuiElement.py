import os
from pathlib import Path

import pygame

from src.GameMethods import GameMethods

LEFT = 1
image_file_formats = [".png", ".jpg", ".jpeg", ".bmp"]

class GuiElement:
    def __init__(self, pos_x, pos_y, width=0, height=0, image=None):
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height
        self.image = image
        self._is_mouse_over = False

        if image is None:

            for format in image_file_formats:
                path = os.path.dirname(os.path.realpath(__file__)) + "/elements/" + self.__class__.__name__.lower() + "/" + self.__class__.__name__ + format
                if Path(path).is_file():
                    break

            try:
                self.image = pygame.image.load(path)
                if self.width == 0 and self.height == height:
                    self.width = self.image.get_rect().width
                    self.height = self.image.get_rect().height
            except:
                pass


    def contains(self, x, y):
        if self.image and self.image.get_rect().collidepoint((x-self.x, y-self.y)):
            return True
        return False

    def on_mouse_down(self):
        pass

    def on_mouse_up(self):
        pass

    def on_mouse_leave(self):
        pass

    def on_hover(self):
        pass

    def update(self, mouse, events, delta_time, keys, config, game_methods: GameMethods):
        if self.contains(*mouse.get_pos()):
            self.on_hover()
            self._is_mouse_over = True
        elif self._is_mouse_over:
            self.on_mouse_leave()
            self._is_mouse_over = False

        if self._is_mouse_over:
            for event in events:
                # Check onMouseDown for left mouse button.
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.on_mouse_down()
                # Check onMouseUp for left mouse button.
                elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    self.on_mouse_up()

    def draw(self, surface):
        if self.image is not None:
            surface.blit(self.image, (self.x, self.y))

    def restart_level(self):
        pass