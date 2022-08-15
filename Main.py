import time
from Tetronimo import Tetronimo
from Grid import *

##game is designed for a square window

# runtime variables
resolution = [500,500]
screen = pygame.display.set_mode(resolution)
piece = Tetronimo("l", [5,5])
timer = 0
scale_vec = [1/20*resolution[0],1/20*resolution[1]]
grid = Grid([1,1], [10,15], (190,220,240))
bgcolor = (200, 230, 255)
running = True

# mainloop
while running:
    time_start = time.time()

    # rendering
    screen.fill(bgcolor)
    grid.render(screen, scale_vec)
    piece.render(screen, scale_vec)
    pygame.display.flip()

    if timer >= 1:
        piece.move([0,1], grid)
        timer = 0

    # inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                piece.rotate(1, grid)
            if event.key == pygame.K_a:
                piece.rotate(-1, grid)
            if event.key == pygame.K_LEFT:
                piece.move([-1, 0], grid)
            if event.key == pygame.K_RIGHT:
                piece.move([1, 0], grid)
            if event.key == pygame.K_DOWN:
                piece.move([0,1], grid)

    time_end = time.time()
    time_elapsed = time_end-time_start
    timer+=time_elapsed
pygame.quit()