import pygame
import sys




w= 800
h=600
screen= pygame.display.set_mode((w,h))

clock= pygame.time.Clock()
running = True


class Player:
    def __init__(self, x, y):
        self.width = 40
        self.height = 60
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.vel = [0, 0]
        self.speed = 5
        self.jump_power = -15
        self.gravity = 1
        self.on_ground = False

class Enemy:
    def __init__(self, x, y, width=40, height=40):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface, scroll_x):
        pygame.draw.rect(surface, RED, (self.rect.x - scroll_x, self.rect.y, self.rect.width, self.rect.height))


player = Player(100, h - 150)
enemies = [Enemy(600,h - 100), Enemy(1100, h- 340)] pygame.init()

pygame.display.set_caption('fario')
platform=[
    pygame.Rect(0,h-40,2000,40),
    pygame.Rect(300,h-80,120,40),
    pygame.Rect(500,h-160,200,40),
    pygame.Rect(700,h-160,200,40),
]
while running:
    clock.tick(60)
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.quit:
            running=False
            pygame.quit()
            sys.exit()
keys = pygame.key.get_pressed()
player.handle_input(keys)

   
Player.apply_physics(platforms)

    
if player.rect.colliderect(enemy.rect):
    if player.vel[1] > 0 and player.rect.bottom <= enemy.rect.top + player.vel[1]:
        enemies.remove(enemy)
        player.vel[1] = player.jump_power // 2  

        scroll_x = player.rect.x - w // 2

    for plat in platform:
        pygame.draw.rect(screen,(0,255,0),(plat.width, plat .h ,plat.x,plat.y))
        pygame.display.flip()
               
