import sys
import pygame
from ship import Ship

from settings import Settings


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.sett = Settings()
        self.width = self.sett.screen_width
        self.height = self.sett.screen_height

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def rungame(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down(event.key)

            elif event.type == pygame.KEYUP:
                self._key_up(event.key)

    def _key_down(self, k):
        if k == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif k == pygame.K_LEFT:
            self.ship.moving_left = True

        elif k == pygame.K_UP:
            self.ship.moving_up = True

        elif k == pygame.K_DOWN:
            self.ship.moving_down = True

        elif k == pygame.K_q:
            sys.exit()

    def _key_up(self, k):
        if k == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif k == pygame.K_LEFT:
            self.ship.moving_left = False

        elif k == pygame.K_UP:
            self.ship.moving_up = False

        elif k == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        self.screen.blit(self.sett.bg, self.screen.get_rect())
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.rungame()


""" elif k == pygame.K_F11 or k == pygame.K_ESCAPE:
            self._toggle_screen(k) """
"""  def _toggle_screen(self, k):
        if k == pygame.K_F11:
            self.width = 1920
            self.height = 1080
            self.screen = pygame.display.set_mode(self.width, self.height)

        if k == pygame.K_ESCAPE:
            self.width = 1200
            self.height = 800
            self.screen = pygame.display.set_mode((self.width, self.height)) """
