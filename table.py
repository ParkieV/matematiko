import pygame
import sys

screen = ''





def main():
    global screen

    pygame.init()

    size = width, height = 800, 640
    screen = pygame.display.set_mode(size)

    screen.fill((255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


if __name__ == "__main__":
    main()
