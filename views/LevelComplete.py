from src import GameMethods
from src.gui.elements.button.Button import Button
from src.gui.elements.text.TextBlock import TextBlock

def load_view(gui, game_methods: GameMethods):
    gui.add_gui_element(TextBlock("You completed the level! :)", 250, 50))
    gui.add_gui_element(TextBlock("Your score was: " + str(game_methods.get_last_level_coins), 280, 75))

    continue_button = Button("Next Level", 300, 150,
                             lambda: game_methods.load_next_level())
    continue_button.resize_button_to_height(50)

    main_menu_button = Button("Main Menu", 300, 250,
                              lambda: game_methods.load_main_menu())
    main_menu_button.resize_button_to_height(50)
    gui.add_gui_element(continue_button)
    gui.add_gui_element(main_menu_button)

