import pygame


class Boy():
    def __init__(self, settings, screen):
        """Инициализирует персонажа и задает его начальное положение."""
        self.settings = settings
        self.screen = screen

        # Загрузка изображения персонажа и получения RECT фигуры
        self.image = pygame.image.load('img/boy.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Настройки появления персонажа
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)

        self.rect.bottom = self.screen_rect.bottom - 30

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False

        # Изменение направления изображения персонажа в зависимости от направления движения
        self.flip_flag = 1
        self.flip_boy()

    def update(self):
        """Обновляет позицию персонажа с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.boy_increment
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.boy_increment
        self.rect.centerx = self.center

    def blitme(self):
        """Рисует персонажа в текущей позиции."""
        self.flip_boy()
        self.screen.blit(self.image, self.rect)

    def flip_boy(self):
        """Меняет направление персонажа."""
        if self.flip_flag == 1 and self.moving_left:
            self.image = pygame.transform.flip(self.image, True, False)
            self.flip_flag -= 1
        if self.flip_flag == 0 and self.moving_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.flip_flag += 1

    def center_boy_x(self):
        self.center = self.screen_rect.centerx

