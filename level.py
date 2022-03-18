
import pygame
from tiles import Tile
from settings import tile_size

class Level:
    def __init__(self,level_data,surface) -> None:
        self.display_surface = surface
        self.setup_level(level_data)
    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for column_index,column in enumerate(row):
                if column == 'X':
                    x = column_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
    
    def run(self):
        self.tiles.draw(self.display_surface)
