import pygame
import sys
import models

LANG = 'ru'
WHITE = (255,255,255)
screen = ''


def main():
    pygame.init()
    global screen
    size = width, height = 800, 640
    screen = pygame.display.set_mode(size)
    RulesWidget = models.Rules()
    MainSurface = models.MainMenu()
    GameWidget = models.Game()
    ChooseWidget = models.Choose()
    MainSurface.draw(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 275 <= x <= 525 and 455 <= y <= 535:
                    sys.exit()
                elif 275 <= x <= 525 and 335 <= y <= 415:
                    RulesWidget.draw(screen)
                    RulesWidget.calls()
                    MainSurface.draw(screen)
                elif 275 <= x <= 525 and 215 <= y <= 295:
                    ChooseWidget.initialization()
                    MainSurface.draw(screen)
        pygame.display.flip()
if __name__ == '__main__':
    main()