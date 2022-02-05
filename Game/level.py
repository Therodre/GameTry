import pygame
from Game import settings
from Game.tile import Tile
from Game.player import Player


class Level:
    def __init__(self):

        # get the screen
        self.display_surface = pygame.display.get_surface()
        # sprite groups
        self.visible_sprite = pygame.sprite.Group()
        self.obstacle_sprite = pygame.sprite.Group()
        self.create_map()

    def create_map(self) -> None:
        for index_row, row in enumerate(settings.WORLD_MAP):
            for index_col, col in enumerate(row):
                x = index_row * settings.TILING
                y = index_col * settings.TILING
                if col == 'x':
                    Tile((x, y), self.visible_sprite)
                elif col == 'p':
                    Player((x, y), self.visible_sprite)

    def run(self):
        self.visible_sprite.draw(self.display_surface)
