import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.sett = ai_game.sett
        self.screen = ai_game.screen
        self.color = ai_game.sett.bullet_color
