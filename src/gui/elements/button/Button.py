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
        self.size_multiplier = 1

    def draw(self, surface):
        super(Button, self).draw(surface)
        (tcx, tcy, icx, icy) = self.text_surface.get_rect().center + self.image.get_rect().center
        surface.blit(self.text_surface, (self.x + icx - tcx, self.y + icy - tcy))

    def resize_button_to_width(self, new_width):
        self.size_multiplier = new_width / self.image.get_rect().width
        self.change_image(self.image)

    def resize_button_to_height(self, new_height):
        self.size_multiplier = new_height / self.image.get_rect().height
        self.change_image(self.image)

    def on_hover(self):
        self.change_image(button_images["light"])

    def on_mouse_down(self):
        self.change_image(button_images["dark"])

    def on_mouse_up(self):
        self.callback()

    def on_mouse_leave(self):
        self.change_image(button_images["green"])

    def change_image(self, image):
        new_width = int(image.get_rect().width * self.size_multiplier)
        new_height = int(image.get_rect().height * self.size_multiplier)
        self.image = pygame.transform.scale(image, (new_width, new_height))