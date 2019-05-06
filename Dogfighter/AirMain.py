import pygame


def draw_hero(screen):
    # load hero image
    hero = pygame.image.load("./images/me1.png")
    # blit function draw image
    screen.blit(hero, (189, 500))


def draw_bg(screen):
    # load background image
    bg = pygame.image.load("./images/background.png")
    # blit function draw image
    screen.blit(bg, (0, 0))


def main():
    # game init
    pygame.init()

    # create game window: 480x700
    screen = pygame.display.set_mode((480, 700))

    # draw background
    draw_bg(screen)
    # draw hero
    draw_hero(screen)

    # update window
    pygame.display.update()

    # game loop
    while True:
        pass

    # game over
    pygame.quit()


if __name__ == '__main__':
    main()

