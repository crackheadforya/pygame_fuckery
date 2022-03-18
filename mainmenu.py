
import pygame,sys
from buttoner import Button
from maingame import Game
from pygame import mixer
class start_menu():
    def __init__(self) -> None:
    
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen_width = 640
        self.screen_height = 360
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        pygame.display.set_caption("radiance")
        self.background = pygame.image.load("assets/titlescreen.png")



        
    def maingame(self):
        while True:
            pygame.mouse.set_visible(True)
            self.playbutton = Button(image = pygame.image.load("assets/play_button.png"),pos=(545,229))
            self.playbutton.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.playbutton.check_for_input(pygame.mouse.get_pos()):
                            self.playbutton.play_music("assets/playbutton.wav")
                            gaem = Game()
                            gaem.game_loop()

                        #print(pygame.mouse.get_pos())

            pygame.display.flip()
            self.screen.blit(self.background,(0,0))
            self.clock.tick(60)

            
menu=start_menu()
menu.maingame()


    
