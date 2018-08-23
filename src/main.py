import pdb

import pygame

from entities.character.Character import Character
from src.Camera import Camera
from src.LevelData import LevelData
from src.level.Level import Level
from tiles.base.Tile import Tile

def getTilePrototypes():
    tilePrototypes = [Tile(0, 0, "Grass")]
    return tilePrototypes

# Spawns a copy of a tileprototype and returns the new one.
def spawnTile(tile, x, y):
    newTile = Tile(x, y, tile.name)
    return newTile

def main():

    level = Level("Level 1")
    level.load()

    pygame.init()
    pygame.display.set_caption("2d platform game it")
    screen = pygame.display.set_mode((1600, 900))
    camera = Camera(screen)

    camera.set_settings(level.config["Camera"])

    running = True
    tile_prototypes = getTilePrototypes()

    DATA = LevelData(98.2 / 24000)
    lastFrameTicks = pygame.time.get_ticks()

    player = Character(200, 200, "character", 1)

    while (running):
        camera.clear()
        for event in pygame.event.get():
            # Check if the quit button has been pressed
            if event.type == pygame.QUIT:
                running = False

        # Calculate deltaTime
        t = pygame.time.get_ticks()
        deltaTime = (t - lastFrameTicks) / 1000.0
        lastFrameTicks = t

        keys = pygame.key.get_pressed()
        DATA.set_keys(keys)

        player.update(deltaTime, DATA)
        camera.render(player)

        # Update

        for entity in level.entities:
            entity.update(deltaTime, DATA)

        # Draw
        for tile in level.tiles:
            camera.render(tile)
        for entity in level.entities:
            camera.render(entity)
        pygame.display.update()

main()