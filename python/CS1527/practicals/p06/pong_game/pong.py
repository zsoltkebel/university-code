import pygame

from settings import Settings
from components import Bat, Ball, Wall
import game_functions as gf

"""
Basic Pong game implemented using pygame.
Does not use pygame.sprite.Sprite features.
Simple animation using image display and background refresh.
"""

def run_game():
    """Main function to start game and run top-level loop"""
    # Initialize pygame, settings and screen object.
    pygame.init()
    # Set keys to repeat if held down.
    pygame.key.set_repeat(25,25)
    # Set a clock to control game frame rate (frame per second)
    clock = pygame.time.Clock()
    # Create settings object containing game settings
    settings = Settings()
    # Create the main game screen
    screen = pygame.display.set_mode( (settings.screen_width, settings.screen_height))
    # Fill the game screen with BLACK colour
    screen.fill(settings.bg_colour)
    # Create a main window caption
    pygame.display.set_caption("CS1527 Pong")

    while settings.lives > 0:

        # Make the wall
        wall = Wall(screen)
        # Make the bat
        bat = Bat(screen, settings)
        # Make the ball
        ball = Ball(screen, settings)
        ball_2 = Ball(screen, settings, x_veloc=10)

         # Start the main loop for the game.
        while ball.rect.centery < settings.screen_height and ball_2.rect.centery < settings.screen_height:
            # Watch for keyboard events.
            gf.check_events(bat)

            # Update the ball to check if it has hit bat or wall
            ball.update(bat, wall, settings)
            ball_2.update(bat, wall, settings)
            
            # Now update the sprites, etc. on the screen
            gf.update_screen(settings, screen, clock, bat, [ball, ball_2], wall)

        # Wait for a key or mouse event to continue
        null_event = pygame.event.wait() 
        settings.lives -= 1

    # GAME ENDS 

# Call the main method to start the game        
run_game()
