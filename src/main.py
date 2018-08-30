import pygame

from src.Game import Game


def main():
    game = Game()
    game.load_level(0)

    get_delta_time = delta_time_gen().__next__

    while tick(get_delta_time(), game):
        continue


def delta_time_gen():
    ticks = pygame.time.get_ticks()
    while True:
        new_ticks = pygame.time.get_ticks()
        yield (new_ticks - ticks) / 1000.0
        ticks = new_ticks


def tick(delta_time, game):
    game.update(delta_time)
    game.render()
    return game.isRunning

main()
