import pygame

# Other game constants
WIDTH = 360
HEIGHT = 480

# define colour
BLACK = (0, 0, 0)

# Create a Ghost sprite class as a subclass of pygame Sprite class
class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Load the image of a ghost and set it as the image for this sprite
        self.image = pygame.image.load('ghost.png')
        # Handle the black background of the sprite (so we don't see it)
        self.image.set_colorkey(BLACK)
        # Get the sprite's rect - and set its location
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        
    # Update method to shift location of sprite's rect
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


class Cake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('cake.png')
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT)

    def update(self, *args, **kwargs):
        self.rect.y += 10
        if self.rect.y > HEIGHT:
            self.rect.y = 0
