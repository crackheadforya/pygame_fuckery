
import pygame,sys
from settings import *
from level import Level
from pygame.locals import *
pygame.init() 
clock = pygame.time.Clock()
pygame.display.set_caption("radiance bone-structure")

#line 11 resizer fnc-> HWSURFACE|DOUBLEBUF|RESIZABLE
screen = pygame.display.set_mode((screen_width,screen_height))
level = Level(level_map,screen)

while True:
    for event in pygame.event.get():             
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    
    screen.fill('black')
    level.run()
    pygame.display.update()
    clock.tick(60)


