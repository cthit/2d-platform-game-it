import pygame
from src.gui.GuiElement import GuiElement

pygame.font.init()

button_images = {
    "light": pygame.image.load("../resources/gui/button_light.png"),
    "dark": pygame.image.load("../resources/gui/button_dark.png"),
    "green": pygame.image.load("../resources/gui/button_green.png"),
    "blue": pygame.image.load("../resources/gui/button_blue.png")
}


class Button(GuiElement):
    def __init__(self, text, pos_x, pos_y, callback, text_color=(255, 255, 255), font=pygame.font.SysFont('Arial', 30)):
        super(Button, self).__init__(pos_x, pos_y, 0, 0, button_images["green"])
        self.font = font
        self.text = text
        self.text_color = text_color
        self.text_surface = font.render(text, True, text_color)
        self.callback = callback

    def draw(self, surface):
        super(Button, self).draw(surface)
        (tcx, tcy, icx, icy) = self.text_surface.get_rect().center + self.image.get_rect().center
        surface.blit(self.text_surface, (self.x + icx - tcx, self.y + icy - tcy))

    def on_hover(self):
        self.image = button_images["light"]

    def on_mouse_down(self):
        self.image = button_images["dark"]

    def on_mouse_up(self):
        self.callback()
