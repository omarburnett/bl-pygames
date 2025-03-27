import pygame
import sys

pygame.init()
w= 800
h=600
screen= pygame.display.set_mode((w,h))

clock= pygame.time.Clock()
running = True

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
    for plat in platform:
        pygame.draw.rect(screen,(0,255,0),(plat.width, plat .height ,plat.x,plat.y))
        pygame.display.flip()
               
