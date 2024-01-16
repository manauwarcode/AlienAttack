import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage the bullet fired from the ship"""

    def __init__(self, aa_game):
        """Create a bullet object at the ship current position"""
        super().__init__()
        self.screen = aa_game.screen
        self.settings = aa_game.settings
        self.color = aa_game.settings.bullet_color

        # Create a bullet at (0,0) and set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = aa_game.ship.rect.midtop

        # Store the bullet position at float
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up the screen"""
        self.y -= self.settings.bullet_speed

        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
