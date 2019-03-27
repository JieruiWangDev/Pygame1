import sys
import pygame

from settings import Settings
def run_game():
    #初始化游戏对象并绘制屏幕
    pygame.init()
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #background color setting
    bg_color = (ai_settings.bg_color)

    #游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)

        pygame.display.flip()

    run_game()



