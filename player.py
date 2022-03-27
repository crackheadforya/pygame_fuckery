import pygame 

class Player(pygame.sprite.Sprite):
    def __init__(self,pos) -> None:
        super().__init__()
        self.image=pygame.Surface((10,20))
        self.image.fill('blue')
        self.rect = self.image.get_rect(bottomleft=pos)

        #player movements
        self.direction = pygame.math.Vector2(0,0)   
        self.speed = 3
        self.gravity = 0.4
        self.jumpy = -4
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction.x=-1
        elif keys[pygame.K_d]:
            self.direction.x=1
        else:
            self.direction.x=0
        
        if keys[pygame.K_SPACE]:
            
            self.jumper_shumper()
            
            
        
    
    def apply_gravity(self):
        self.direction.y +=self.gravity
        self.rect.y +=self.direction.y
    def jumper_shumper(self):
        
        self.direction.y = self.jumpy
        

    def update(self):
        self.get_input()
        
       
    