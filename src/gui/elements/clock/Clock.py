import numpy as np

from src.GameMethods import GameMethods
from src.gui.GuiElement import GuiElement
from src.gui.elements.counter.Counter import Counter


class Clock(GuiElement):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, 0, 0)
        self.counter = Counter(pos_x, pos_y, lambda: self.formatted_time, prefix="LevelTime:  ")
        self.time = 0
        self.formatted_time = ""

    def update(self, mouse, events, delta_time, keys, config, game_methods: GameMethods):
        self.time += delta_time
        time_in_sec = self.time
        milli_seconds = int(time_in_sec * 100) % 100
        seconds = int(time_in_sec % 60)
        time_in_min = (time_in_sec - seconds) / 60
        minutes = int(time_in_min % 60)
        hours = int((time_in_min - minutes) / 60)
        self.formatted_time = str(hours) + ":" + str(minutes) + ":" + str(seconds) + ":" + str(milli_seconds)
        self.counter.update(mouse, events, delta_time, keys, config, game_methods)

    def draw(self, surface):
        self.counter.draw(surface)

