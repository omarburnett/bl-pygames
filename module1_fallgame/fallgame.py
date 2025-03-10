import pygame
import random

pygame.init()
height= 1000
width= 1200
RED =(255,0,0)
WHITE=(255,255,255) 
BLUE=(0,0,204)
screen=pygame.display.set_mode((width,height))

pygame.display.set_caption('avoid falling stuff')

clock = pygame.time.Clock()
fps= 60

running=True
#objects are just values

class Player:
    def _init_(self):
        self.x = width // 2
        self.y= height - player_height - 10
        self.player_width =50
        self.player_height=50
        self.playerspeed=5
    
    def move(self,keys):
        if keys[pygame.K_LEFT]and self.x > 0:
            self.x -=self.playerspeed
        if keys[pygame.K_RIGHT]and self.x < width - self.playerwidth:
            self.x+=self.playerspeed
    
    def draw (self):
        pygame.draw.rect(screen,BLUE, (self.x, self.y,self.playerwidth, self.playerheight))

class fallingobjects:
    def __init__(self):
        self.x= random.randint(0,width - 50)
        self.y = -50
        self.width=50
        self.height=50
        self.speed=random.randint(3,7)
    def move(self):
        self.y += self.speed
        pygame.draw.rect(screen,RED,(self.x,self.y, self.width, self.height))

player = Player()
falling_object=[]
score=0
lives=3

while running:

    clock.tick(fps)
    screen.fill(WHITE)
    
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw()

    
    if random.randint(1, 30) == 1:  
        falling_objects.append(FallingObject())

    
    for obj in falling_objects[:]:
        obj.move()
        obj.draw()

        
        if (obj.x < player.x + player.width and
            obj.x + obj.width > player.x and
            obj.y < player.y + player.height and
            obj.y + obj.height > player.y):
            lives -= 1
            falling_objects.remove(obj)  

    
        elif obj.off_screen():
            falling_objects.remove(obj)
            score += 1  

    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

    if lives <= 0:
        game_over_text = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(game_over_text, (width // 2 - 50, height // 2))
        pygame.display.update()
        pygame.time.delay(2000)  
        running = False

    pygame.display.update() 

pygame.quit()       
          
pygame.display.update()       



