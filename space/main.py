import pygame
import sys
from kernel import foo
from configs import HEIGHT, WIDTH
from ship import createSpaceship

# Initialize Pygame
pygame.init()

# Screen dimensions

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Viewer")

# Load spaceship image (replace 'spaceship.png' with your actual file path)
try:
    spaceship_img = pygame.image.load('images/ship-small.png').convert_alpha()
except pygame.error as e:
    print("Error loading image:", e)
    pygame.quit()
    sys.exit()

# Spaceship position and movement
x, y = WIDTH // 2, HEIGHT // 2
speed = 5

#initialize Game Objects
spaceship = createSpaceship("Player")
game_objects = [spaceship]

def steer_ship():
    """Function to steer the ship using keyboard controls."""
    global x, y
    
    # Get pressed keys
    keys = pygame.key.get_pressed()
    
    # Movement controls - Arrow keys or WASD
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed
    
    # Keep spaceship within screen bounds
    x = max(0, min(x, WIDTH))
    y = max(0, min(y, HEIGHT))

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))  # Black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Call the steering function (currently empty)
    #steer_ship()
    
    # Call the foo function from kernel
    #foo()

    # Draw the spaceship
    #spaceship_rect = spaceship_img.get_rect(center=(x, y))
    #screen.blit(spaceship_img, spaceship_rect)

    for game_object in game_objects:
        game_object.epochEvent(game_objects)

    for game_object in game_objects:
        if game_object.isAlive():
            draw_data = game_object.getDrawData(distroyed=False)
            screen.blit(draw_data[0], draw_data[1])
        else:
            #to remove distryed objects or bullets 
            game_objects.remove(game_object)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()

