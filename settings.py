import pygame


import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (53, 28, 69)
        self.bg = pygame.image.load("media/background.bmp")
        # self.bg = pygame.transform.scale(self.bg, (1920, 1080))
        self.ship_speed = 1.5

        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (46, 103, 248)
