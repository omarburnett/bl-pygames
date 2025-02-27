import pygame
import random
pygame.init()
height=1000
width=1200
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('avoid falling stuff')
clock = pygame.time.Clock()
fps=60
running=True
while running:
    for event in pygame.event.get():

        if event.type==pygame.quit:
            running=False
  
pygame.quit()

#objects are just values
class player:
    def_init_(self)
    self.x = width // 2
    self.y= height -60
    self.playerwidth =50
    self.playerheight=50
    self.playerspeed=5
def move(self,keys):
    if keys[pygame.l_LEFT]and self.x > 0:
        self.x -=self.playerspeed
    if keys[pygame.K_RIGHT]and self.x < width - self.playerwidth:
        self.x+=self.playerspeed
def draw(self):
    pygame.draw.rect(screen,(0,0,225),(self.x,self.y self.width self.height))
