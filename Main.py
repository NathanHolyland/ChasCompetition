import time
import pygame
from random import *
from GameWindow import *
from Menu import *
from dataclasses import dataclass

@dataclass
class KeyState:
    state: bool
    should_reset: bool

##game is designed for a square window

# runtime variables
resolution = [500,500]
screen = pygame.display.set_mode(resolution)

time_elapsed = 0
clock = pygame.time.Clock()
FPS = 15

running = True

#UI elements
game = GameWindow(resolution)
menu = Menu()

# inputs Format .active, .should_reset
keys = {
    pygame.K_LEFT: KeyState(False, False),
    pygame.K_RIGHT: KeyState(False, False),
    pygame.K_DOWN: KeyState(False, False),
    pygame.K_d: KeyState(False, True),
    pygame.K_a: KeyState(False, True)
}

# mainloop
menu.menuMusic()
while running:
    time_start = time.perf_counter()

    # rendering
    game.render(screen)
    menu.render(screen)
    pygame.display.flip()

    # events
    game.update(time_elapsed)
    game.userInput(keys)

    # input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key].state = True

        elif event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key].state = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttons = menu.checkButtons(pygame.mouse.get_pos())
            if buttons["play"]:
                menu.close()
                game.start()

    clock.tick(FPS)
    time_end = time.perf_counter()
    time_elapsed = time_end-time_start

pygame.quit()