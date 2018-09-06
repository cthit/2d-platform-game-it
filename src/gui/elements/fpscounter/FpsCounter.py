import numpy as np

from src.GameMethods import GameMethods
from src.gui.GuiElement import GuiElement
from src.gui.elements.counter.Counter import Counter


class FpsCounter(GuiElement):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, 0, 0)
        self.counter = Counter(pos_x, pos_y, lambda: self.fps, prefix="FPS: ")
        self.num_frames = 20
        self._i = 0
        self.frames = []
        self.fps = 0

    def update(self, mouse, events, delta_time, keys, config, game_methods: GameMethods):
        self._i = (self._i + 1) % self.num_frames
        frame_time = 1 / delta_time
        self.frames.insert(self._i, frame_time)
        self.fps = int(np.array(self.frames).mean())
        self.counter.update(mouse, events, delta_time, keys, config, game_methods)

    def draw(self, surface):
        self.counter.draw(surface)

