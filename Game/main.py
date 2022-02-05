# !~\anaconda3\envs\Game_try\python.exe


import pygame
from sys import exit
from Game import settings
from Game.tile import Tile
from Game.level import Level
from Game.player import *
from Game.level import Level


class Game:
    _WIDTH = settings.WIDTH
    _HEIGHT = settings.HEIGHT

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('My1stcrush')
        self.screen = pygame.display.set_mode((self._WIDTH, self._HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
        pass

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # print(event)
                    pygame.quit()
                    exit()
            self.screen.fill('Black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(settings.FPS)


if __name__ == '__main__':
    game = Game()
    game.run()

