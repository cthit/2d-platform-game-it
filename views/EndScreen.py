from src.GameMethods import GameMethods
from src.gui.elements.button.Button import Button
from src.gui.elements.text.TextBlock import TextBlock


def load_view(gui, game_methods: GameMethods):
    gui.add_gui_element(TextBlock("You Win!", 200, 200))
    gui.add_gui_element(Button("Restart Game", 300, 100, lambda: game_methods.load_level_by_index(1)))
