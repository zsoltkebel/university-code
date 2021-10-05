import sys
import pygame

pygame.font.init() 

def check_events(bat):
    """Respond to key presses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move bat right
                bat.move_right()
            elif event.key == pygame.K_LEFT:
                # Move bat left
                bat.move_left()

def update_screen(settings, screen, clock, bat, balls, wall):
    """Update objects on the screen.""" 
    # Refresh the screen's background colour'
    screen.fill(settings.bg_colour)

    # Refresh the display of the 3 game objects
    wall.blitme()
    bat.blitme()
    for ball in balls:  # modified part for multiple balls
        ball.blitme()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()

    # Tick the clock - using 30 frames per second
    clock.tick(30)
    
