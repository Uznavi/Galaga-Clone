import pygame
import constants as c
import random
from bullet import Bullet

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()
        self.image = pygame.image.load("enemy sprite 2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//13, self.image.get_height()//13))
        self.is_invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.snd_hit = pygame.mixer.Sound("hit_sound.ogg")
        self.hp = 1
        self.bullets = pygame.sprite.Group()
        self.bullet_timer_max = 60
        self.bullet_timer = self.bullet_timer_max
        self.states = {"FLY_DOWN" : "FLY_DOWN", "ATTACK": "ATTACK"}
        self.state = self.states["FLY_DOWN"]
        self.init_state = True
        self.score_value = 5
        self.vel_x = 0
        self.vel_y = random.randrange(3,4)
    def update(self):
        if self.state == "FLY_DOWN":
            self.state_fly_down()
        elif self.state == "ATTACK":
            self.state_attack()
        self.rect.x+=self.vel_x
        self.rect.y +=self.vel_y
        self.bullets.update()

    def state_fly_down(self):
        if self.init_state:
            self.init_state = False
        if self.rect.y >= 200:
            self.state = self.states["ATTACK"]
            self.init_state = True

    def state_attack(self):
        if self.init_state:
            self.vel_y = 0
            while self.vel_x == 0:
                self.vel_x = random.randrange(-4,4)
            self.init_state = False
        if self.bullet_timer == 0:
            self.shoot()
            self.bullet_timer = self.bullet_timer_max
        else:
            self.bullet_timer -=1
        if self.rect.x <= 0:
            self.vel_x *=-1
        elif self.rect.x >= c.DISPLAY_WIDTH-50:
            self.vel_x *=-1

    def get_hit(self):
        self.snd_hit.play()
        self.hp-=1
        if self.hp <=0:
            self.destroy()

    def destroy(self):
        self.kill()
    def shoot(self):
        new_bullet = Bullet()
        new_bullet.vel_y = 4
        new_bullet.rect.x = self.rect.x+ (self.rect.width/2)
        new_bullet.rect.y = self.rect.y + self.rect.height
        self.bullets.add(new_bullet)

        #TODO: Change the color of the exploding particles, just make that shit white.
