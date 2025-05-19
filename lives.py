import pygame
import constants as c

class Lives(pygame.sprite.Sprite):
    def __init__(self, num_lives):
        super(Lives, self).__init__()
        self.num_lives = 3
        self.width = 80
        self.height = 40
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.image.set_colorkey((0,0,0))
        self.ship_image = pygame.image.load("ship sprite.png").convert_alpha()
        self.ship_image = pygame.transform.scale(self.ship_image, (self.ship_image.get_width()//35,
                                                                        self.ship_image.get_height()//35))
        self.image.blit(self.ship_image, (0, 0))
        self.font_size = 24
        self.font = pygame.font.Font(None,self.font_size)
        self.font_color = (255,255,255)
        self.lives_counter = self.font.render(f"x{self.num_lives}", False, self.font_color, False)
        self.image.blit(self.lives_counter, (40,10))
        self.rect = self.image.get_rect()
        self_vel_x = 0
        self_vel_y = 0


    def update(self):
        pass

    def decrement_life(self): #Removes lives
        self.num_lives -=1
        if self.num_lives <0:
            self.num_lives = 0
        else:
            self.image = pygame.Surface(self.size)
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(self.ship_image, (0, 0))
            self.lives_counter = self.font.render(f"x{self.num_lives}", False, self.font_color, False)
            self.image.blit(self.lives_counter, (40, 10))
#Dude I'm gonna be real here, idfk how this is running. The HP and Lives are reversed
#but as a wise man once said, "Fuck it, we ball"
