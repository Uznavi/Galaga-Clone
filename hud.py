import pygame
import constants as c
from score import Score
from lives import Lives

class HUD(pygame.sprite.Sprite):
    def __init__(self, num_lives):
        super(HUD, self).__init__()
        self.image = pygame.image.load("HUD.png").convert_alpha() #TODO: Remove this later and just add everything to the bottom
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//1.5, self.image.get_height()//1.5))
        self.rect = self.image.get_rect()
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.vel_x = 0
        self.vel_y = 0
        self.score = Score()
        self.lives = Lives(num_lives)
        self.lives.rect.x = 275
        self.lives.rect.y = c.DISPLAY_HEIGHT - 40
        self.score_group = pygame.sprite.Group()
        self.icons_group = pygame.sprite.Group()
        self.score_group.add(self.score)
        self.icons_group.add(self.lives)

    def update(self):
        self.score_group.update()
        self.icons_group.update()
        self.rect.x += self.vel_x
        self.rect.y +=self.vel_y

        #Add a high score here

