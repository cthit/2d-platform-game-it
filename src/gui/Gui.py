import pygame

class Gui:
    def __init__(self):
        self.gui_elements = list()

    def update(self, mouse, events):
        for element in self.gui_elements:
            if element.contains(mouse.get_pos):
                element.on_hover()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass