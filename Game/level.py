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
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = YSortCameraGroup()
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
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        #  debug(self.player.direction)
        debug(self.visible_sprites.offset.magnitude())


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2  # getting the x coord of the screen
        self.half_height = self.display_surface.get_size()[1] // 2  # getting the y coord of the screen
        self.offset: pygame.math.Vector2 = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = -player.rect.centerx + self.half_width
        self.offset.y = -player.rect.centery + self.half_height
        for sprite in sorted(self.sprites(), key=lambda sprite : sprite.hitbox.centery):
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image, offset_pos)

