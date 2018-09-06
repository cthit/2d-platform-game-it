from behaviours.Collector import Collector
from entities.base.Entity import Entity
from src.GameMethods import GameMethods
from src.gui.elements.clock.Clock import Clock
from src.gui.elements.counter.Counter import Counter
from src.gui.elements.fpscounter.FpsCounter import FpsCounter
from src.gui.elements.text.TextBlock import TextBlock
from src.gui.elements.timelimit.TimeLimit import TimeLimit


def load_view(gui, game_methods: GameMethods):
    gui.add_gui_element(FpsCounter(20, 20))
    gui.add_gui_element(Counter(20, 320, lambda: game_methods.get_player_coins(), prefix="Coins: "))
    gui.add_gui_element(Clock(20, 420))
    level_time = game_methods.get_level().level_time
    if level_time > 0:
        gui.add_gui_element(TimeLimit(300, 20, level_time))
