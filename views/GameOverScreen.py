from src import GameMethods
from src.gui.elements.button.Button import Button
from src.gui.elements.text.TextBlock import TextBlock


def load_view(gui, game_methods: GameMethods):
    gui.add_gui_element(TextBlock("You lost :(", 300, 50))
    retry_button = Button("Retry Level", 300, 150,
                          lambda: game_methods.load_level_by_index(game_methods.get_previous_level_index()))
    retry_button.resize_button(200, 50)
    main_menu_button = Button("Main Menu", 300, 250,
                              lambda: game_methods.load_main_menu())
    main_menu_button.resize_button(200, 50)
    gui.add_gui_element(retry_button)
    gui.add_gui_element(main_menu_button)