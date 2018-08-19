import pygame

from entities.character.Character import Character


def main ():
    pygame.init()

    pygame.display.set_caption("2d platform game it")
    screen = pygame.display.set_mode((1600, 900))
    running = True

    lastFrameTicks = 0
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate deltaTime
        t = pygame.time.get_ticks()
        deltaTime = (t - lastFrameTicks) / 1000.0
        lastFrameTicks = t
        apa = Character(0, 0, "character", 1)


main();