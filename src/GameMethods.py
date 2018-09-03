class GameMethods:
    def __init__(self, game):
        self.find_entities = lambda name: game.level.get_entities(name)
        self.restart_level = lambda: game.reload_entities()
        self.go_to_next_level = lambda: game.load_next_level()
        self.get_level_dimensions = lambda: game.level.map_shape[::-1]
        self.load_level_by_index = lambda index: game.load_level(index)
