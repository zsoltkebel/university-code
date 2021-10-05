# Basic pygame sprites solution
import pygame
import sys
from sprites import Ghost, Cake

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colour
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Sprites in pygame")

clock = pygame.time.Clock()

# Create a sprite Group to hold/manage sprite objects
all_sprites = pygame.sprite.Group()
# Create an instance of the ghost sprite
ghost = Ghost()
# Create the falling cake
cake = Cake()
# Add the instance to our sprite group
all_sprites.add(ghost)
all_sprites.add(cake)

# Main game loop
while True:
    # Keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Update all (only 1) sprites
    all_sprites.update()
    
    # Draw / render the sprites on the screen
    screen.fill(BLUE)
    all_sprites.draw(screen)
    
    # Flip the display
    pygame.display.flip()

    if pygame.sprite.collide_mask(ghost, cake) is not None:
        cake.rect.y = 0

pygame.quit()

 
