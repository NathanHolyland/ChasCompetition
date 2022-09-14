import numpy as np
import pygame
from math import *

patterns = {
    "i": [[[0.5,-0.5],[1.5,-0.5],[-0.5,-0.5],[-1.5,-0.5]],(0,220,255)],
    "l": [[[0,0],[-1,0],[1,0],[1,-1]],(255,70,0)],
    "j": [[[0,0],[1,0],[-1,0],[-1,-1]],(20,0,255)],
    "o": [[[-0.5,0.5],[-0.5,-0.5],[0.5,0.5],[0.5,-0.5]],(240,255,0)],
    "s": [[[0,0],[0,-1],[-1,0],[1,-1]],(26,255,0)],
    "z": [[[0,0],[0,-1],[1,0],[-1,-1]], (255,0,0)],
    "t": [[[0,0],[1,0],[-1,0],[0,-1]], (100,0,255)]
}

class Tetronimo:
    def __init__(self, type, position):
        self.position = position
        self.tiles = patterns[type][0]
        self.color = patterns[type][1]

        self.activeTimer = False
        self.timerLimit = 0.25
        self.timer = 0

    def move(self, vec, grid):
        self.position[0] += vec[0]
        self.position[1] += vec[1]
        if not grid.validatePosition(self, vec):
            self.position[0] -= vec[0]
            self.position[1] -= vec[1]
        elif self.activeTimer:
            self.timer = 0
            self.timerLimit -= 0.025

    def rotate(self, direction, grid):
        matrix = np.array([[0,-direction],[direction,0]])
        new_tiles = []

        #apply 2d rotation matrix to every point (works because they are all relative)
        for i in range(len(self.tiles)):
            vec = np.asarray(self.tiles[i])
            new_vec = np.matmul(matrix, vec)
            new_tiles.append(new_vec.tolist())
        
        previous = self.tiles.copy()
        self.tiles = new_tiles

        if not grid.validatePosition(self, [0,0]):
            self.tiles = previous

    def render(self, surface, scale):
        pos = self.position
        for tile in self.tiles:
            pygame.draw.rect(surface, self.color, [(pos[0]+tile[0])*scale[0], (pos[1]+tile[1])*scale[1], scale[0], scale[1]], 0)
            pygame.draw.rect(surface, (0, 0, 0), [(pos[0]+tile[0])*scale[0], (pos[1]+tile[1])*scale[1], scale[0], scale[1]], 1)


