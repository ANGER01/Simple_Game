import pygame
from tools import *

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Square")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 55, 55)
SIZE = 50
X_MID = WIDTH // 2 - SIZE // 2
Y_MID = HEIGHT // 2 - SIZE // 2
# Square settings
player = Player(X_MID, Y_MID)
block = Block(X_MID + 60, Y_MID + 60)

blocks = []

clock = pygame.time.Clock()
running = True
all_visible = []
all_visible.append(player)

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys


    player.player_move()

    
    # Keep the square inside the window
    player.rect.x = max(0, min(player.rect.x, WIDTH - SIZE))
    player.rect.y = max(0, min(player.rect.y, HEIGHT - SIZE))

    # Draw everything
    screen.fill(BLACK)

    block_group.draw(screen)
    player_group.draw(screen)
    
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

pygame.quit()