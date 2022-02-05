import pygame
from Game import settings
from Game.tile import Tile
from Game.player import Player
from debug import debug

class Level:
    def __init__(self):

        # get the screen
        self.display_surface = pygame.display.get_surface()
        # sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()
        self.player: Player

    def create_map(self) -> None:
        for index_row, row in enumerate(settings.WORLD_MAP):
            for index_col, col in enumerate(row):
                x = index_row * settings.TILING
                y = index_col * settings.TILING
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], obstacle_sprites=self.obstacle_sprites)

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)
