from src.GameMethods import GameMethods
from src.gui.GuiElement import GuiElement
from src.gui.elements.counter.Counter import Counter

class TimeLimit(GuiElement):
    def __init__(self, pos_x, pos_y, level_time):
        super().__init__(pos_x, pos_y, 0, 0)
        self.counter = Counter(pos_x, pos_y, lambda: self.formatted_time, prefix="Time Left:  ")
        self.time = float(level_time)
        self.formatted_time = ""

    def update(self, mouse, events, delta_time, keys, config, game_methods: GameMethods):
        self.time -= delta_time
        if self.time <= 0:
            game_methods.restart_level()

        time_in_sec = int(self.time)
        time_in_milli = int(self.time * 1000)
        self.formatted_time = str(time_in_sec) + ":" + str(time_in_milli)