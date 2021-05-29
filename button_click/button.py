import pygame.font


class Button:
    """Класс управляющий изображением кнопок на кэране."""

    def __init__(self, screen, msg):
        """Инициализирует атрибуты кнопки."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Назначение размеров и свойств кнопок
        self.width, self.height = 200, 50
        self.button_color = 200, 0, 200
        self.text_color = 255, 255, 255
        self.font = pygame.font.SysFont(None, 35)

        # Построение объекта rect кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки создается только один раз
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Преобразует сообщение в прямоугольник и выравнивает его по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Отображение пустой кнопки перед выводом сообщения
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
