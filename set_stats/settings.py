import pygame


class SettingsGame:
    """Класс для хранения настроек игры."""

    def __init__(self):
        """Инициализирует настройки игры."""

        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 100, 20)  # Задание цвета фонового окна
        self.icon = pygame.image.load('img/icon.jpg')

        # Настройки класса Boy
        self.boy_increment = 7
        self.life_limit = 3

        # Настройки класса Boll
        self.boll_increment = 3
        self.boll_allowed = 1

        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        # Настройки уровня
        self.level_score_limit = 5
        self.level_flag = self.level_score_limit

    def initialize_dynamic_settings(self):
        """Инициализирует динамические настройки игры."""
        self.boy_increment = 7
        self.boll_increment = 3
        self.boll_allowed = 1

        # Подсчет очков
        self.level_score_limit = 5
        self.points = 1

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимости пришельцев."""
        self.boll_increment *= self.speedup_scale
        self.boy_increment *= self.speedup_scale
        self.points = int(self.points)

        if self.level_flag == 0:
            self.level_score_limit = int(self.level_score_limit + self.score_scale)
            self.level_flag = self.level_score_limit
            self.boll_allowed += 1
