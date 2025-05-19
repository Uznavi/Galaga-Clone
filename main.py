import pygame
from ship import Ship
import constants as c
from background import BG
from enemy_spawner import EnemySpawner
from particle_spawner import ParticleSpawner
from event_handler import EventHandler

#Pygame Initialization
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
pygame.font.init()

#Display setup
display = pygame.display.set_mode(c.DISPLAY_SIZE)
fps = 60
clock = pygame.time.Clock()
black = (0,0,0)

#Object setup

bg = BG()
player = Ship()
bg_group = pygame.sprite.Group()
bg_group.add(bg)
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
enemy_spawner = EnemySpawner()
particle_spawner = ParticleSpawner()
event_handler = EventHandler()


running =  True
while running:
    clock.tick(fps) #Tick clock

    #Handle Events
    event_handler.handle_events(player)

    #Update all the objects
    sprite_group.update()
    bg_group.update()
    enemy_spawner.update()
    particle_spawner.update()

    #Check collision
    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()
        player.hud.score.update_score(enemy[0].score_value)
        if not enemy[0].is_invincible:
            particle_spawner.spawn_particles((bullet.rect.x, bullet.rect.y))
    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        if not enemy[0].is_invincible and not player.is_invincible:
            player.get_hit()
            enemy[0].hp = 0
            enemy[0].get_hit()


    #Render the display
    display.fill(black)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    particle_spawner.particle_group.draw(display)
    player.hud_group.draw(display)
    player.hud.icons_group.draw(display)
    player.hud.score_group.draw(display)
    pygame.display.update()


