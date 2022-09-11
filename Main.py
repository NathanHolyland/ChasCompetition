import time
import pygame
from Tetronimo import Tetronimo
from Grid import *
from random import *
from UI import *

##game is designed for a square window

def randomPiece():
    options = ["i","l","j","o","s","z","t"]
    i = randrange(0, 6)
    pos = [5, 2]
    if options[i] == "i" or options[i] == "o":
        pos = [5.5, 1.5]
    return Tetronimo(options[i], pos)

# runtime variables
resolution = [500,500]
screen = pygame.display.set_mode(resolution)
piece = randomPiece()
timer = 0
scale_vec = [1/19*resolution[0],1/19*resolution[1]]
grid = Grid([1,1], [10,15], (190,220,240))
bgcolor = (200, 230, 255)
running = True
clock = pygame.time.Clock()
FPS = 15

#UI elements
scoreboard = ...

# inputs
keys = {
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False,
    pygame.K_DOWN: False
}

# mainloop
while running:
    time_start = time.perf_counter()

    # rendering
    screen.fill(bgcolor)
    grid.render(screen, scale_vec)
    piece.render(screen, scale_vec)
    pygame.display.flip()

    # events
    if timer >= 1:
        piece.move([0,1], grid)
        timer = 0
    
    if (piece.timer >= piece.timerLimit) or piece.timerLimit <= 0:
        grid.commitTetronimo(piece, [1,1])
        piece = randomPiece()

    clears = grid.clearCheck()
    for line in clears:
        grid.clearRow(line)


    # input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            for k in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN):
                if event.key == k:
                    keys[k] = True

            if event.key == pygame.K_d:
                piece.rotate(1, grid)
            if event.key == pygame.K_a:
                piece.rotate(-1, grid)

        elif event.type == pygame.KEYUP:
            for k in (pygame.K_d, pygame.K_a, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN):
                if event.key == k:
                    keys[k] = False
            

    if keys[pygame.K_LEFT]:
        piece.move([-1, 0], grid)
    if keys[pygame.K_RIGHT]:
        piece.move([1, 0], grid)
    if keys[pygame.K_DOWN]:
        piece.move([0,1], grid)

    

    clock.tick(FPS)
    time_end = time.perf_counter()
    time_elapsed = time_end-time_start
    timer+=time_elapsed
    if piece.activeTimer:
        piece.timer += time_elapsed


pygame.quit()