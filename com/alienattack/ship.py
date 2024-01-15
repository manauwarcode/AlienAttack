import pygame


class Ship:
    def __init__(self, aa_game):
        """Initialize the ship and set its starting position"""
        self.screen = aa_game.screen
        self.settings = aa_game.settings
        self.screen_rect = aa_game.screen.get_rect()

        # load the ship image from the images folder
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # start new ship from the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store the float for ship exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up:
            self.y -= self.settings.ship_speed
        if self.moving_down:
            self.y += self.settings.ship_speed

        #update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)
