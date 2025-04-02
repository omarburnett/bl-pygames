import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Endless Runner")

player_image = pygame.image.load("glass ball.jpg")
obstacle_image = pygame.image.load("glass ball.jpg")
background_image = pygame.image.load("glass ball.jpg")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        w=4
        h=4
        
        
        
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (50, screen_height - 50)
        self.y_velocity = 0
        self.gravity = 0.8
        self.jump_strength = -20

    def update(self):
        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.y_velocity = 0

    def jump(self):
        self.y_velocity = self.jump_strength

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacle_image
        self.rect = self.image.get_rect()
        self.rect.x = screen_width + 50
        self.rect.y = screen_height - 50
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

clock = pygame.time.Clock()
running = True
score = 0
obstacle_timer = 0
obstacle_interval = 1500

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Update
    all_sprites.update()

    obstacle_timer += clock.get_time()
    if obstacle_timer > obstacle_interval:
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)
        obstacle_timer = 0
        obstacle_interval = max(500, obstacle_interval - 50)
    
    if pygame.sprite.spritecollideany(player, obstacles):
        running = False

    # Draw
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    score += 1
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score // 10), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()  