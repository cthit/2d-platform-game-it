import pygame

from entities.character.Character import Character
from src.LevelData import LevelData
from tiles.base.Tile import Tile

def getTilePrototypes():
    tilePrototypes = [Tile(0, 0, "Grass")]
    return tilePrototypes

# Spawns a copy of a tileprototype and returns the new one.
def spawnTile(tile, x, y):
    newTile = Tile(x, y, tile.name)
    return newTile

def main():
    #level = Level("Level 1")
    #level.load()

    pygame.init()
    pygame.display.set_caption("2d platform game it")
    screen = pygame.display.set_mode((1600, 900))
    running = True
    tile_prototypes = getTilePrototypes()
    tiles = []
    for i in range(0, screen.get_width(), 21):
        # Spawns a floor of grass at the bottom of the screen.
        tiles.append(spawnTile(tile_prototypes[0], i, (screen.get_height() - 21)))


    DATA = LevelData(98.2)
    lastFrameTicks = 0

    player = Character(200, 200, "character", 10)

    while (running):
        screen.fill((100, 100, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate deltaTime
        t = pygame.time.get_ticks()
        deltaTime = (t - lastFrameTicks) / 1000.0
        lastFrameTicks = t
        player.update(deltaTime, DATA)
        player.draw(screen)
        for tile in tiles:
            tile.draw(screen)
        pygame.display.update()

main()