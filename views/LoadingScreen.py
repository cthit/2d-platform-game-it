import os

import pygame

from src.gui.elements.image.Image import Image
from src.gui.elements.text.TextBlock import TextBlock


def load_view(gui, game):
    gui.add_gui_element(TextBlock("Loading next level", 200, 200))
    path = os.path.dirname(os.path.realpath(__file__)) + "/../resources/funtique/FuntiqueGUI_0001_Loader.png"
    loading_image = pygame.image.load(path)
    gui.add_gui_element(Image(200, 250, loading_image))
