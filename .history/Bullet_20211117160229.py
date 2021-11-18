import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.sett = ai_game.sett
        self.screen = ai_game.screen
        self.color = ai_game.sett.bullet_color
        self.ship = ai_game.ship

        self.rect = self.rect(0, 0, self.sett.bullet_width, self.sett.bullet_height)

        self.rect.midtop = self.ship.image_rect.midtop

    def draw_bullet(self):
        pygame.draw.rect(self.screen)

