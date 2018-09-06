from behaviours.Collector import Collector
from entities.base.Entity import Entity
from src.GameMethods import GameMethods
from src.gui.elements.clock.Clock import Clock
from src.gui.elements.counter.Counter import Counter
from src.gui.elements.fpscounter.FpsCounter import FpsCounter
from src.gui.elements.text.TextBlock import TextBlock

def load_view(gui, game_methods: GameMethods):
    gui.add_gui_element(FpsCounter(20, 20))
    gui.add_gui_element(Counter(20, 320, lambda: get_player_coins(game_methods), prefix="Coins: "))
    gui.add_gui_element(Clock(20, 420))

def get_player_coins(game_methods: GameMethods):
    player: Entity = game_methods.find_entities("Player")[0]
    return player.get_behaviour(Collector).get_num_collected("Coin")
