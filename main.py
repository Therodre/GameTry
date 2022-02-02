import pygame
from sys import exit


class Game:
    _WIDTH = 800
    _HEIGHT = 400

    def __init__(self):
        pass

    def run(self):
        pygame.init()
        pygame.display.set_caption('My1stcrush')
        screen = pygame.display.set_mode((self._WIDTH, self._HEIGHT))
        clock = pygame.time.Clock()
        _width_surface, _height_surface = 20, 20
        test_surface = pygame.Surface((_width_surface, _height_surface))
        test_surface.fill(color='Red')

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
