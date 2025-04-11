import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

second_obstacle_width = 600
second_obstacle_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
screen2 = pygame.display.set_mode((second_obstacle_width,second_obstacle_height))

pygame.display.set_caption("Endless Runner")

# Colors
black = (255, 255, 255, 255)

# Player properties
player_x = 50
player_y = 450
player_width = 50
player_height = 80
player_speed_y = 0
gravity = 1
is_jumping = False

#player image 
player_image = pygame.image.load("KTTYCAT.webp").convert()
# Obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacles = []

# Background properties
background_x = 0
background_speed = 3
background_image = pygame.image.load("KTTYCAT.webp").convert() # Replace with your image file

# Game variables
score = 0
game_over = False
clock = pygame.time.Clock()

# Functions
def draw_player():
    pygame.draw.rect(screen, black,   (player_x, player_y, player_width, player_height))

def generate_obstacle():
    obstacle_x = screen_width
    obstacle_y = 500 
    obstacle_2y=500
    obstacle_2x=second_obstacle

    obstacles.append([obstacle_x, obstacle_y,obstacle_2x, obstacle_2y])
    
def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, black, (obstacle[0], obstacle[1],obstacle[0],obstacle[1], obstacle_width, obstacle_height))

def move_obstacles():
    for obstacle in obstacles:
        obstacle[0] -= obstacle_speed

def check_collision():
    for obstacle in obstacles:
        if player_x < obstacle[0] + obstacle_width and \
           player_x + player_width > obstacle[0] and \
           player_y < obstacle[1] + obstacle_height and \
           player_y + player_height > obstacle[1]:
                return True
    return False







def display_score():
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, (10, 10))

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                player_speed_y = -20
                is_jumping = True
            if event.key == pygame.K_r and game_over:
                # Restart the game
                game_over = False
                score = 0
                player_x = 50
                player_y = 450
                player_speed_y = 0
                is_jumping = False
                obstacles = []

    if not game_over:
        # Player movement
        player_speed_y += gravity
        player_y += player_speed_y
        if player_y >= 450:
            player_y = 450
            player_speed_y = 0
            is_jumping = False

        # Obstacle generation
        if len(obstacles) == 0 or obstacles[-1][0] < screen_width - 200:
            generate_obstacle() 
            
       

        # Move background
        background_x -= background_speed
        if background_x <= -background_image.get_width():
            background_x = 0

         # Move obstacles
        move_obstacles()

        # Collision check
        if check_collision():
            game_over = True

        # Score update
        score += 1

        # Remove off-screen obstacles
        obstacles = [obstacle for obstacle in obstacles if obstacle[0] > -obstacle_width]

    # Drawing
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + background_image.get_width(), 0))
    draw_player()
    draw_obstacles()
    display_score()

    if game_over:
         font = pygame.font.Font(None, 72)
         text = font.render("Game Over!", True, black)
         text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
         screen.blit(text, text_rect)

         score_text = font.render("Score: " + str(score), True, black)
         score_rect = score_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
         screen.blit(score_text, score_rect)

         restart_text = pygame.font.Font(None, 36).render("Press 'R' to restart", True, black)
         restart_rect = restart_text.get_rect(center=(screen_width // 2, screen_height // 2 + 120))
         screen.blit(restart_text, restart_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
