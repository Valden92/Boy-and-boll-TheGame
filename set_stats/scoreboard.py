import pygame.font
from pygame.sprite import Group
from boy.life_class import BoyLife


class Scoreboard():
    """Класс для вывода игровой информации и статистики."""

    def __init__(self, settings, screen, stats):
        """Инициализирует атрибуты подсчета очков."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Настройки шрифта для вывода счета
        self.num_color = 200, 200, 200
        self.text_color = 255, 255, 255
        self.num_font = pygame.font.SysFont(None, 40)
        self.text_font = pygame.font.SysFont(None, 40)

        # Подготовка исходного изображения
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lifes()


    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        rounded_score = self.stats.score
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.num_font.render(score_str, True, self.num_color, self.settings.bg_color)

        # Вывод счета в правой верхней чайсти экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        # Вывод текста около счета
        self.score_text = self.text_font.render('Score:', True, self.text_color, self.settings.bg_color)
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.right = self.score_rect.left - 20
        self.score_text_rect.top = self.score_rect.top

    def show_score(self):
        """Выводит счет, рекорд и число оставшихся кораблей на экран."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.score_text, self.score_text_rect)

        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.high_score_text, self.high_score_text_rect)

        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.level_text, self.level_text_rect)
        self.lifes.draw(self.screen)

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        high_score = self.stats.high_score
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.num_font.render(high_score_str, True,
                                                 self.num_color, self.settings.bg_color)
        # Рекорд выравнивается по центру с верхней стороны
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

        # Вывод текста около лучшего счета
        self.high_score_text = self.text_font.render('High Score:', True, self.text_color, self.settings.bg_color)
        self.high_score_text_rect = self.high_score_text.get_rect()
        self.high_score_text_rect.right = self.high_score_rect.left - 20
        self.high_score_text_rect.top = self.score_rect.top

    def prep_level(self):
        """Преобразует счетчик уровня в изображение."""
        self.level_image = self.num_font.render(str(self.stats.level), True,
                                            self.num_color, self.settings.bg_color)
        # Уровень выводится под текущим счетом
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

        # Вывод текста около счета
        self.level_text = self.text_font.render('Level:', True, self.text_color, self.settings.bg_color)
        self.level_text_rect = self.level_text.get_rect()
        self.level_text_rect.right = self.level_rect.left - 20
        self.level_text_rect.top = self.level_rect.top

    def prep_lifes(self):
        """Количество оставшихся жизней."""
        self.lifes = Group()
        for life_num in range(self.stats.life):
            life = BoyLife()
            life.rect.x = 20 + life_num * life.rect.width
            life.rect.y = 10
            self.lifes.add(life)