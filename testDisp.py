import pygame
import time
from Tetronimo import Tetronimo

def drawTetronimo(surface, Tetronimo, scale):
    pos = Tetronimo.position
    for tile in Tetronimo.getTiles():
        pygame.draw.rect(surface, Tetronimo.color, [pos[0]+(tile[0]*scale), pos[1]+(tile[1]*scale), scale, scale], 0)


screen = pygame.display.set_mode([500, 500])
piece = Tetronimo("j", [250,250])
timer = 0
running = True
while running:
    time_start = time.time()
    screen.fill((255, 255, 255))
    drawTetronimo(screen, piece, 20)
    pygame.display.flip()

    if timer >= 1:
        piece.move([0,20])
        timer = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                piece.rotate(1)
            if event.key == pygame.K_a:
                piece.rotate(-1)

    time_end = time.time()
    time_elapsed = time_end-time_start
    timer+=time_elapsed
pygame.quit()