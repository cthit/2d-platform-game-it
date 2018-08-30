import pygame
from src.gui.GuiElement import GuiElement

pygame.font.init()


class TextBlock(GuiElement):
    def __init__(self, text, pos_x, pos_y, color=(255, 255, 255), font=pygame.font.SysFont('Arial', 30)):
        super(TextBlock, self).__init__(pos_x, pos_y, 0, 0)
        self.font = font
        self.text = text
        self.color = color
        self.text_surface = font.render(text, True, color)

    def draw(self, surface):
        surface.blit(self.text_surface, (self.x, self.y))
