import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("media/heroship.bmp")
        self.image = pygame.transform.scale(self.image, (80, 120))
        self.image_rect = self.image.get_rect()
        self.speed = ai_game.sett.ship_speed

        self.image_rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

        self.x = float(self.image_rect.x)
        self.y = float(self.image_rect.y)

    def update(self):
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.x += self.speed
        elif self.moving_left and self.image_rect.left > 0:
            self.x -= self.speed
        elif self.moving_up and self.image_rect.top > self.screen_rect.top:
            self.y -= self.speed
        elif self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        self.image_rect.x = self.x
        self.image_rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
