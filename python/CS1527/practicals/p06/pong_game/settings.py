BLACK = (0, 0, 0)

class Settings():
       """A class to store all top-level game settings for Pong."""
       def __init__(self):
           """Initialize the game's settings."""

           # Screen settings
           self.screen_width = 800
           self.screen_height = 500

           # Background 
           self.bg_colour = BLACK

           # Game settings
           self.lives = 3