import os

import pygame


class GuiElement:
    def __init__(self, pos_x, pos_y, width=0, height=0, image=None):
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height
        self.image = image

        if image is None:
            path = os.path.dirname(os.path.realpath(__file__)) + "/elements/" + self.__class__.__name__ + "/" + self.__class__.__name__ + ".png"
            try:
                self.image = pygame.image.load(path)
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

    def on_hover(self):
        pass

    def draw(self, surface):
        if self.image is not None:
            surface.blit(self.image, (self.x, self.y))
