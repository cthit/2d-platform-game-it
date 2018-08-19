import pygame

from entities.character.Character import Character
from src.LevelData import LevelData
from tiles.base.Tile import Tile


def main ():
    pygame.init()
    pygame.display.set_caption("2d platform game it")
    screen = pygame.display.set_mode((1600, 900))
    running = True

    DATA = LevelData(98.2)
    lastFrameTicks = 0

    player = Character(200, 200, "character", 10)
    grassTile1 = Tile(500, 500, "Grass")

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
        grassTile1.draw(screen)
        pygame.display.update()

main();