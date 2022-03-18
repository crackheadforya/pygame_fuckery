import pygame,sys
from crosshair import Crosshair

class Game():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.playing =True
        self.display_width,self.display_height = 640,360
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption("radiance-play")
        self.background = pygame.image.load("assets/background.png")
        pygame.mouse.set_visible(False)
        self.crosshair = Crosshair("assets/crosshair_new.png")

        self.crosshair_group = pygame.sprite.Group()
        self.crosshair_group.add(self.crosshair)

    def game_loop(self):
        while self.playing:
            self.check_events()
            pygame.display.flip()
            self.screen.blit(self.background,(0,0))
            self.crosshair_group.draw(self.screen)
            self.crosshair_group.update()
            self.clock.tick(60)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running,self.playing = False,False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False

#gmingg=Game()
#gmingg.game_loop()


