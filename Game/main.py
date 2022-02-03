import pygame
from sys import exit
from Game import settings
from Game.tile import Tile


class Game:
    _WIDTH = settings.WIDTH
    _HEIGHT = settings.HEIGHT

    def __init__(self):
        self.visible_sprite = pygame.sprite.Group()
        pass

    def run(self):
        pygame.init()
        pygame.display.set_caption('My1stcrush')
        screen = pygame.display.set_mode((self._WIDTH, self._HEIGHT))
        clock = pygame.time.Clock()
        _width_surface, _height_surface = 20, 20
        test_surface = pygame.Surface((settings.TILING, settings.TILING))
        test_surface.fill(color='Red')
        for index_y, y in enumerate(settings.WORLD_MAP):
            for index_x, x in enumerate(y):
                if x == 'x':
                    Tile((x, y), [self.visible_sprite])

        while True:
            # do a barrel roll
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # print(event)
                    pygame.quit()
                    exit()
            screen.blit(test_surface, (20, 20))
            pygame.display.update()
            clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# while True:
#     # do a barrel roll
#     for event in pygame.event.get():
#         if event == pygame.QUIT:
#             pygame.quit()
#             exit()
#     pygame.display.update()
