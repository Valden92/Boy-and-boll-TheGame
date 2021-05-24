import sys
import pygame
from time import sleep
from random import randint
from boll.boll_class import Boll



# ОБНОВЛЕНИЕ ЭКРАНА И ВЗАИМОДЕЙСТВИЕ С КЛАВИАТУРОЙ

def check_keydown_events(event, settings, screen, stats, boy, bolls, sb):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        boy.moving_right = True
    elif event.key == pygame.K_LEFT:
        boy.moving_left = True
    elif event.key == pygame.K_ESCAPE:
        stats.save_high_score()
        sys.exit()
    elif stats.game_active == False and event.key == pygame.K_p:
        start_new_game(settings, screen, stats, bolls, sb)


def check_keyup_events(event, boy):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_RIGHT:
        boy.moving_right = False
    elif event.key == pygame.K_LEFT:
        boy.moving_left = False


def check_events(settings, screen, stats, boy, bolls, play_button, sb):
    """Отслеживание событий клавиатуры и мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats.save_high_score()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, stats, boy, bolls, sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, boy)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, bolls, play_button, sb, mouse_x, mouse_y)



def update_screen(settings, screen, stats, boy, bolls, play_button, sb):
    """Обновляет изображения на экране и отображает новый экран."""
    screen.fill(settings.bg_color)  # Перерисовка экрана в соответсвиии с заданным цветом bg_color
    boy.blitme()
    sb.show_score()
    for boll in bolls.sprites():
        boll.draw_boll()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


# ПРОЧИЕ ФУНКЦИИ

def start_new_game(settings, screen, stats, bolls, sb):
    stats.reset_stats()
    settings.initialize_dynamic_settings()
    pygame.mouse.set_visible(False)

    sb.prep_score()
    sb.prep_level()
    sb.prep_lifes()

    stats.game_active = True
    bolls.empty()
    create_boll(settings, screen, bolls)


def check_play_button(settings, screen, stats, bolls, play_button, sb, mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнокпи PLay."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Скрытие указателя мыши
        start_new_game(settings, screen, stats, bolls, sb)


def boy_lost(settings, screen, stats, boy, bolls, sb):
    """Обработка пропущенных обектов и остановка игры в случае проигрыша."""
    if stats.life >= 1:
        stats.life -= 1
        sb.prep_lifes()
        bolls.empty()
        create_boll(settings, screen, bolls)
        boy.center_boy_x()
        sleep(0.5)
    if stats.life == 0:
        stats.game_active = False
        pygame.mouse.set_visible(True)


# РАБОТА С ПАДАЮЩИМИ ОБЪЕКТАМИ

def create_boll(settings, screen, bolls):
    """Создает один мяч."""
    boll = Boll(settings, screen)
    boll.rect.y = 0 - boll.rect.height
    boll.rect.x = randint(70, settings.screen_width - 70)
    bolls.add(boll)

# def create_bolls(settings, screen, bolls):
#     """Создает ряд мячей."""
#     if len(bolls) < settings.boll_allowed:
#         if settings.boll_allowed > 1:
#             for num in range(settings.boll_allowed):
#                 create_boll(settings, screen, bolls)
#         else:
#             create_boll(settings, screen, bolls)


def bolls_update(settings, screen, stats, boy, bolls, sb):
    """Обновляет позиции мячей."""
    bolls.update()
    for boll in bolls.copy():
        if boll.rect.y > settings.screen_height:
            bolls.remove(boll)
            create_boll(settings, screen, bolls)
        boy_collide_boll(settings, screen, stats, boy, bolls, boll, sb)
    check_bolls_bottom(settings, screen, stats, boy, bolls, sb)


def boy_collide_boll(settings, screen, stats, boy, bolls, boll, sb):
    """Обрабатывает столкновение персонажа и падающего объекта."""
    if pygame.sprite.spritecollideany(boy, bolls):
        stats.score += settings.points
        sb.prep_score()
        check_high_score(stats, sb)
        level_up(settings, stats, sb)
        bolls.remove(boll)
        create_boll(settings, screen, bolls)


def check_bolls_bottom(settings, screen, stats, boy, bolls, sb):
    """Проверяет пропущенные падающие объекты."""
    screen_rect = screen.get_rect()
    for boll in bolls.sprites():
        if boll.rect.bottom >= screen_rect.bottom:
            boy_lost(settings, screen, stats, boy, bolls, sb)
            break


# ОБРАБОТКА И ВЕДЕНИЕ СЧЕТА

def check_high_score(stats, sb):
    """Проверяет появился ли новый рекорд."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def level_up(settings, stats, sb):
    """Увеличивает уровень."""
    settings.level_flag -= 1
    if settings.level_flag == 0:
        stats.level += 1
        sb.prep_level()
        settings.increase_speed()



