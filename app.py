# main.py
import pygame
from utils.Path import Path
from utils.MovingObject import MovingObject

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a road (path) with direction 'right' (can be 'left', 'up', or 'down')
road = Path(100, 100, 600, 400, direction='right')

# Create a moving object
moving_obj = MovingObject(150, 150, 50, 50, (255, 0, 0), 5, 5, road)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move and draw everything
    moving_obj.move()
    
    screen.fill((0, 0, 0))  # Clear screen with black
    road.draw(screen)  # Draw the road
    moving_obj.draw(screen)  # Draw the moving object
    
    pygame.display.flip()  # Update the screen
    pygame.time.Clock().tick(60)  # Limit frame rate to 60 FPS

pygame.quit()
