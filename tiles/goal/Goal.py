from tiles.base.Tile import Tile


class Goal(Tile):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
