import pygame
from Tetronimo import Tetronimo
from Grid import *
from random import *
from UI import *

##game is designed for a square window

def randomPiece():
    options = ["i","l","j","o","s","z","t"]
    i = randrange(0, 7)
    pos = [5, 2]
    if options[i] == "i" or options[i] == "o":
        pos = [5.5, 1.5]
    return Tetronimo(options[i], pos)

def selectPiece(type):
    pos = [5, 2]
    if type == "i" or type == "o":
        pos = [5.5, 1.5]
    return Tetronimo(type, pos)

class GameWindow:
    def __init__(self, resolution, flags):
        self.active = False
        self.flags = flags

        self.heldPiece = None
        self.activePiece = randomPiece()
        self.timer = 0
        self.scale_vec = [1/19*resolution[0],1/19*resolution[1]]
        self.grid = Grid([1,1], [10,15], (190,220,240), flags)
        self.bgcolor = (200, 230, 255)
        self.running = True

        self.score = 0
        self.scoreboard = TextLabel((200,200,220), pygame.font.SysFont('calibri', 25), str(self.score), (255, 0, 0), [300, 50, 150, 25], True)

    def start(self):
        self.active = True

    def setScore(self, score):
        self.score = score
        self.scoreboard.changeText((255, 0, 0), str(score))

    def newPiece(self):
        self.activePiece = randomPiece()
        if not self.grid.validatePosition(self.activePiece, [0, 0]):
            self.flags["gameOver"] = True

    def holdPiece(self):
        prev_held = self.heldPiece
        self.heldPiece = selectPiece(self.activePiece.type)
        self.heldPiece.position = [13.2, 6]
        if prev_held:
            self.activePiece = selectPiece(prev_held.type)
        else:
            self.newPiece()

    def update(self, dt):
        if not self.active:
            return

        if self.timer >= 1:
            self.activePiece.move([0,1], self.grid)
            self.timer = 0
    
        if (self.activePiece.timer >= self.activePiece.timerLimit) or self.activePiece.timerLimit <= 0:
            self.grid.commitTetronimo(self.activePiece, [1,1])
            self.newPiece()

        clears = self.grid.clearCheck()
        for line in clears:
            self.grid.clearRow(line)
        if 4 > len(clears) > 0:
            self.flags["lineClear"] = True
        elif len(clears) == 4:
            self.flags["tetris"] = True
        if len(clears) > 0:
            scores = [100, 300, 500, 800]
            self.setScore(self.score+scores[len(clears)-1])
        
        self.timer+=dt
        if self.activePiece.activeTimer:
            self.activePiece.timer += dt

    def userInput(self, keys):
        if not self.active:
            return

        bound_actions = {
            pygame.K_LEFT: ["move", [-1, 0]],
            pygame.K_RIGHT: ["move", [1, 0]],
            pygame.K_DOWN: ["move", [0, 1]],
            pygame.K_d: ["rotate", 1],
            pygame.K_a: ["rotate", -1],
            pygame.K_SPACE: ["drop"],
            pygame.K_RETURN: ["hold"]
        }

        for key in keys:
            if keys[key].state:
                if bound_actions[key][0] == "move":
                    self.activePiece.move(bound_actions[key][1], self.grid),
                elif bound_actions[key][0] == "rotate":
                    self.activePiece.rotate(bound_actions[key][1], self.grid)
                elif bound_actions[key][0] == "hold":
                    self.holdPiece()
                elif bound_actions[key][0] == "drop":
                    valid_move = [0,0]
                    for dy in range(20):
                        if self.grid.validateMove(self.activePiece,[0, dy]):
                            valid_move = [0, dy]
                        else:
                            break
                    self.activePiece.move(valid_move, self.grid)
                    self.grid.commitTetronimo(self.activePiece, [1, 1])
                    self.flags["hardDrop"] = True
                    self.newPiece()
                if keys[key].should_reset:
                    keys[key].state = False
    
    def render(self, screen):
        if not self.active:
            return
        screen.fill(self.bgcolor)
        self.grid.render(screen, self.scale_vec)
        self.activePiece.render(screen, self.scale_vec)
        pygame.draw.rect(screen, (0, 0, 0), [300, 100, 120, 120], 2)
        if self.heldPiece:
            self.heldPiece.render(screen, self.scale_vec)
        self.scoreboard.render(screen)