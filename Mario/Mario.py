import pygame
import sys
import random


pygame.init()

screen_width = 800
screen_height = 600


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario-like Game Example")


white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
brown = (165, 42, 42)
black = (0, 0, 0)


player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5


obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_frequency = 25  


ground_height = 50


gravity = 1


jump = False
jump_count = 10


obstacles = []


clock = pygame.time.Clock()

def draw_ground_and_sky():
    pygame.draw.rect(screen, green, (0, screen_height - ground_height, screen_width, ground_height))
    pygame.draw.rect(screen, blue, (0, 0, screen_width, screen_height - ground_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > player_speed:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width - player_speed:
        player_x += player_speed
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jump = False
            jump_count = 10

    
    if player_y < screen_height - player_height:
        player_y += gravity
    else:
        player_y = screen_height - player_height

  
    if random.randint(1, obstacle_frequency) == 1:
        obstacle_x = random.randrange(0, screen_width - obstacle_width)
        obstacle_y = -obstacle_height
        obstacles.append([obstacle_x, obstacle_y])

 
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

    
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < screen_height]

    
    for obstacle in obstacles:
        if (
            player_x < obstacle[0] + obstacle_width
            and player_x + player_width > obstacle[0]
            and player_y < obstacle[1] + obstacle_height
            and player_y + player_height > obstacle[1]
        ):
            pygame.quit()
            sys.exit()

   
    screen.fill(white)
    draw_ground_and_sky()
    pygame.draw.rect(screen, black, (player_x, player_y, player_width, player_height))

    
    for obstacle in obstacles:
        pygame.draw.rect(screen, brown, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

   
    pygame.display.flip()

   
    clock.tick(30)
 