from src.GameMethods import GameMethods
from src.gui.elements.button.Button import Button
from src.gui.elements.text.TextBlock import TextBlock


# TODO eliassu 2018-08-31: replace game with a variable that exposes a safe subset of game
def load_view(gui, game_methods: GameMethods):
    gui.add_gui_element(TextBlock("This is a text block!", 100, 100))
    gui.add_gui_element(Button("Start Game", 100, 150, lambda: game_methods.load_level_by_index(1)))
