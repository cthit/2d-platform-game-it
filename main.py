import pygame

def main ():
    pygame.init()

    pygame.display.set_caption("2d platform game it")
    screen = pygame.display.set_mode((800, 450))
    running = True

    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

main()