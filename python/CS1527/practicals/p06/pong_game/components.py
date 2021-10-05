import pygame
import random

class Ball():
    def __init__(self, screen, settings, x_veloc=5, y_veloc=5):
        """Initialize the ball"""

        # Keep a local copy of the screen
        self.screen = screen
        # Load the ball image and get its pygame rect.
        self.image = pygame.image.load('images/ballGrey.png')
        self.rect = self.image.get_rect()

        # Start each new ball at a random position 
        self.rect.centerx = random.randint(50, settings.screen_width - 50)
        self.rect.centery = random.randint(100, 400)

        # Start each new ball with an x & y velocity of 5
        self.x_veloc = x_veloc
        self.y_veloc = y_veloc

    def update(self, bat, wall, settings):
        """ Update the ball status"""
        status = self.bounce(bat, wall, settings)
        if status == 'Right' or status == 'Left':
            self.x_veloc = -1 * self.x_veloc
        elif status == 'Wall' or status == 'Bat':
            self.y_veloc = -1 * self.y_veloc  

        # Update the x,y position of the ball
        self.rect.centerx += self.x_veloc
        self.rect.centery += self.y_veloc

    def blitme(self):
        """Draw the ball at its current location."""
        self.screen.blit(self.image, self.rect)

    def bounce(self, bat, wall, settings):
        """Determine if the ball has bounced and if so, on what."""
        if self.rect.top <= wall.rect.bottom:
            self.rect.top = wall.rect.bottom
            return 'Wall'
        elif self.rect.left <= 0:
            self.rect.left = 0
            return 'Left'
        elif self.rect.right >= settings.screen_width:
            self.rect.right = settings.screen_width
            return 'Right'
        elif self.rect.bottom >= bat.rect.top:
            if (self.rect.centerx >= bat.rect.left) and (self.rect.centerx <= bat.rect.right):
                self.rect.bottom = bat.rect.top
                return 'Bat'
        else: return False

class Bat():
    def __init__(self, screen, settings):
        """Initialize the bat"""

        #Keep a local copy of the screen
        self.screen = screen
        # Load the bat image and get its pygame rect.
        self.image = pygame.image.load('images/bat.png')
        self.rect = self.image.get_rect()

        # Start each new bat at the centre bottom of the screen.
        self.rect.centerx = settings.screen_width / 2
        self.rect.top = settings.screen_height - 50

    def move_right(self):
        """Move the bat 20 pixels to the right."""
        if self.rect.centerx <= 730:
            self.rect.centerx += 20

    def move_left(self):
        """Move the bat 20 pixels to the left."""
        if self.rect.centerx > 70:
            self.rect.centerx -= 20

    def blitme(self):
        """Draw the bat at its current location."""
        self.screen.blit(self.image, self.rect)

class Wall():
    def __init__(self, screen):
        """Initialize the wall"""

        # Keep a local copy of the screen
        self.screen = screen

        # Load the wall image and get its pygame rect.
        self.image = pygame.image.load('images/wall.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set the position of the wall image rect - sp it appears at screen top
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def blitme(self):
        """Draw the wall at its fixed location."""
        self.screen.blit(self.image, self.rect)

