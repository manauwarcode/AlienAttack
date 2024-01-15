import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Attack")
        self.ship = Ship(self)
        self.bg_color = self.settings.bg_color

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.ship.moving_left = True
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.ship.moving_up = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.ship.moving_down = True
                if event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.ship.moving_left = False
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.ship.moving_down = False
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    aa = AlienInvasion()
    aa.run_game()
