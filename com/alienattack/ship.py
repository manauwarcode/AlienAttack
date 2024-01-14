import pygame


class Ship:
    def __init__(self, aa_game):
        """Initialize the ship and set its starting position"""
        self.screen = aa_game.screen
        self.screen_rect = aa_game.screen.get_rect()

        # load the ship image from the images folder
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # start new ship from the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y +=1

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)
