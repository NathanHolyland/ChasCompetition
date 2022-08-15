import time
from Tetronimo import Tetronimo
from Grid import *
from random import *

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

    # inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pieceMoved = False
            if event.key == pygame.K_d:
                piece.rotate(1, grid)
                pieceMoved = True
            if event.key == pygame.K_a:
                piece.rotate(-1, grid)
                pieceMoved = True
            if event.key == pygame.K_LEFT:
                piece.move([-1, 0], grid)
                pieceMoved = True
            if event.key == pygame.K_RIGHT:
                piece.move([1, 0], grid)
                pieceMoved = True
            if event.key == pygame.K_DOWN:
                piece.move([0,1], grid)
                pieceMoved = True
            
            if pieceMoved and piece.activeTimer:
                piece.timer = 0
                piece.timerLimit -= 0.025

    time_end = time.time()
    time_elapsed = time_end-time_start
    timer+=time_elapsed
    if piece.activeTimer:
        piece.timer += time_elapsed
pygame.quit()