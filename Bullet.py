import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.sett = ai_game.sett
        self.screen = ai_game.screen
        self.color = ai_game.sett.bullet_color
        self.ship = ai_game.ship

        self.bullet_rect = self.rect(
            0, 0, self.sett.bullet_width, self.sett.bullet_height
        )

        self.bullet_rect.midtop = self.ship.image_rect.midtop
        self.y = float(self.bullet_rect.y)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_rect, self.color)

