import pygame
from pygame.locals import *
import sys
import pygwidgets
from Game import Game   # now Blackjack Game

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

background = pygwidgets.Image(window, (0, 0), 'images/background.png')

oGame = Game(window)

while True:
    for event in pygame.event.get():
        if ((event.type == QUIT) or
            ((event.type == KEYDOWN) and (event.key == K_ESCAPE))):
            pygame.quit()
            sys.exit()

        oGame.handle_event(event)

    background.draw()
    oGame.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)