import pygame

LEFT = 1

class Gui:
    def __init__(self):
        self.gui_elements = list()

    def update(self, mouse, events):
        curr_element = None
        for element in self.gui_elements:
            if element.contains(mouse.get_pos):
                curr_element = element
                element.on_hover()

        if curr_element is not None:
            for event in events:
                # Check onMouseDown for left mouse button.
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    curr_element.on_mouse_down()
                # Check onMouseUp for left mouse button.
                elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    curr_element.on_mouse_up()

        curr_element = None

    def add_gui_element(self, gui_element):
        self.gui_elements.append(gui_element)

    def draw(self, screen):
        for element in self.gui_elements:
            element.draw(screen)