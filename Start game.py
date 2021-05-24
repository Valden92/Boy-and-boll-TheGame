import pygame
from pygame.sprite import Group
from set_stats.settings import SettingsGame
from boy.boy_class import Boy
from set_stats.game_stats import GameStats
from button_click.button import Button
from set_stats.scoreboard import Scoreboard
import function as gf


def run_game():
    """Инициализирует игру и создает объект экрана."""
    pygame.init()
    settings = SettingsGame()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_icon(settings.icon)
    pygame.display.set_caption("Boy and Boll")
    clock = pygame.time.Clock()

    # Создание экземпларов статистики
    stats = GameStats(settings)
    play_button = Button(screen, "Press P for Start")
    sb = Scoreboard(settings, screen, stats)

    # Создание объектов и групп объектов
    boy = Boy(settings, screen)
    bolls = Group()
    gf.create_boll(settings, screen, bolls)

    # Запуск основного цикла игры
    while True:
        clock.tick(100)
        gf.check_events(settings, screen, stats, boy, bolls, play_button, sb)
        gf.update_screen(settings, screen, stats, boy, bolls, play_button, sb)
        if stats.game_active:
            boy.update()
            gf.bolls_update(settings, screen, stats, boy, bolls, sb)


run_game()
