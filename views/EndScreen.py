from src.GameMethods import GameMethods
from src.gui.elements.button.Button import Button
from src.gui.elements.text.TextBlock import TextBlock


# TODO eliassu 2018-08-31: replace game with a variable that exposes a safe subset of game
def load_view(gui, game_methods: GameMethods):
    gui.add_gui_element(TextBlock("You Win!", 200, 200))
