from src import GameMethods
from src.gui.elements.button.Button import Button
from src.gui.elements.text.TextBlock import TextBlock

def load_view(gui, game_methods: GameMethods):
    gui.add_gui_element(TextBlock("You completed the level! :)", 250, 50))
    num_coins = game_methods.get_last_level_coins()
    text = "You collected " + str(num_coins)
    if num_coins == 1:
        text = text + " coin"
    else:
        text = text + " coins"

    gui.add_gui_element(TextBlock(text, 265, 90))

    if game_methods.last_level_time_left > 0:
        text_2 = "You had " + "{:.3f}".format(game_methods.last_level_time_left) + "s left."
        gui.add_gui_element(TextBlock(text_2, 265, 140))


    continue_button = Button("Next Level", 300, 190,
                             lambda: game_methods.load_next_level())
    continue_button.resize_button(200, 50)

    main_menu_button = Button("Main Menu", 300, 290,
                              lambda: game_methods.load_main_menu())
    main_menu_button.resize_button(200, 50)
    gui.add_gui_element(continue_button)
    gui.add_gui_element(main_menu_button)

