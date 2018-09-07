from src.GameMethods import GameMethods
from src.gui.elements.button.Button import Button
from src.gui.elements.text.TextBlock import TextBlock


def load_view(gui, game_methods: GameMethods):
    button_width = 200
    button_height = 50

    button_one = Button("Level One", 300, 50, lambda: game_methods.load_level_by_index(1))
    button_one.resize_button(button_width, button_height)

    button_two = Button("Level Two", 300, 150, lambda: game_methods.load_level_by_index(2))
    button_two.resize_button(button_width, button_height)

    button_three = Button("Level Three", 300, 250, lambda: game_methods.load_level_by_index(3))
    button_three.resize_button(button_width, button_height)

    button_four = Button("Level Four", 300, 350, lambda: game_methods.load_level_by_index(4))
    button_four.resize_button(button_width, button_height)

    gui.add_gui_element(button_one)
    gui.add_gui_element(button_two)
    gui.add_gui_element(button_three)
    gui.add_gui_element(button_four)

