import pygame
from pygame.sprite import Sprite


class BoyLife(Sprite):
    def __init__(self):
        """Инициализирует графическое отображение жизней."""
        super().__init__()
        self.image = pygame.image.load('img/heart.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.width // 30, self.height // 30))
        self.rect = self.image.get_rect()
