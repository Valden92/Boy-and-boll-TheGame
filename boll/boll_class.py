import pygame
from pygame.sprite import Sprite


class Boll(Sprite):
    """Класс генерации мячей."""

    def __init__(self, settings, screen):
        """Инициализирует мяч и задает начальную позицию."""
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('img/boll_img.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # self.rect.y = random.randrange(-500, -10)

        self.drop_factor = self.settings.boll_increment
        self.rect.x = self.rect.width
        self.rect.y = self.screen_rect.top - self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение мяча по координате Y."""
        self.y += self.drop_factor
        self.rect.y = self.y

    def draw_boll(self):
        """Выводит изображение на экран."""
        self.screen.blit(self.image, self.rect)
