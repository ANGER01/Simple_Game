import pygame
from tools import Player

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

blocks = [pygame.Rect(X_MID + 60, Y_MID + 60, SIZE/2, SIZE/2)]
clock = pygame.time.Clock()
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    player.player_move(keys, blocks)

    
    # Keep the square inside the window
    player.body.x = max(0, min(player.body.x, WIDTH - SIZE))
    player.body.y = max(0, min(player.body.y, HEIGHT - SIZE))

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player.body)
    pygame.draw.rect(screen, RED, blocks[0])
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

pygame.quit()