import pygame

# _sounds = {}

class GameMethods:
    def __init__(self, game):
        self.find_entities = lambda name: game.level.get_entities(name)
        self.restart_level = lambda: game.restart_level()
        self.go_to_next_level = lambda: game.load_next_level()
        self.get_level_dimensions = lambda: game.level.map_shape[::-1]
        self.load_level_by_index = lambda index: game.load_level(index)
        self.spawn_entity = lambda entity, x, y, *args: game.level.spawn_entity(entity, x, y)
        self.kill_entity = lambda entity: game.level.kill_entity(entity)

    def play_sound(self, file_name: str):
        if file_name is not None:
            #if not file_name in _sounds:
            sound = pygame.mixer.Sound("../resources/sound/"+file_name)
            sound.play()
            #    _sounds[file_name] = sound
            #_sounds[file_name].play()