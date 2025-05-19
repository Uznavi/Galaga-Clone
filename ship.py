import pygame
import constants as c
from bullet import Bullet
from hud import HUD

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load("ship sprite.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//30, self.image.get_height()//30))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH//2
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height * 2
        self.bullets = pygame.sprite.Group()
        self.snd_shoot = pygame.mixer.Sound("shooting_sound.ogg")
        self.lives = 3
        self.hud = HUD(self.lives)
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.is_invincible = False
        self.max_invincible_timer = 150
        self.invincible_timer = 0

        #Remove the invincible stuff later. When the player gets killed, have the game wait
        #Like, 3 seconds, before starting up again, no invincibility in this bitch
        self.hp = 1
        self.hud = HUD(self.hp)
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5

    def update(self): #for all sprites
        self.rect.x +=self.velocity_x
        self.rect.y += self.velocity_y
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >=c.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = c.DISPLAY_WIDTH - self.rect.width
        self.bullets.update()
        self.hud_group.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)

        #Check for invisibility
        if self.invincible_timer > 0:
            self.invincible_timer -=1
        else:
            self.is_invincible = False
        print(self.is_invincible)

    def shoot(self):
        self.snd_shoot.play()
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + (self.rect.width//2) - 3
        new_bullet.rect.y = self.rect.y
        self.bullets.add(new_bullet)
        #Add code to make the bullets stop. Don't spam bullets

    def get_hit(self):
        self.hp-=1
        if self.hp <= 0:
            self.hp = 0
            self.death()
        print(f"HP: {self.hp}")
    def death(self):
        self.lives -=1
        print(f"Lives: {self.lives}")
        if self.lives <=0:
            self.lives = 0
        self.hp = 1
        self.hud.lives.decrement_life()
        self.rect.x = c.DISPLAY_WIDTH // 2
        self.is_invincible = True
        self.invincible_timer = self.max_invincible_timer

        #At some point, remove the invincibility and just create like an explosion animation
        #or like a break or something

