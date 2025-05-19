import pygame
import constants as c
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("enemy sprite 1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//13, self.image.get_height()//13))
        self.is_invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.snd_hit = pygame.mixer.Sound("hit_sound.ogg")
        self.hp = 1
        self.score_value = 5
        self.vel_x = 0
        self.vel_y = random.randrange(3,8)
    def update(self):
        self.rect.x+=self.vel_x
        self.rect.y +=self.vel_y
    def get_hit(self):
        self.snd_hit.play()
        self.hp-=1
        if self.hp <=0:
            self.destroy()

    def destroy(self):
        self.kill()

        #TODO: Change the color of the exploding particles, just make that shit white.
