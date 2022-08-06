import numpy as np
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

    def move(self, vec):
        self.position[0] += vec[0]
        self.position[1] += vec[1]
    
    def getTiles(self):
        return self.tiles
    
    def rotate(self, direction):
        matrix = np.array([[0,-direction],[direction,0]])
        new_tiles = []
        for i in range(len(self.tiles)):
            vec = np.asarray(self.tiles[i])
            new_vec = np.matmul(matrix, vec)
            new_tiles.append(new_vec.tolist())
        self.tiles = new_tiles
            
i_shape = Tetronimo("i", [0,0])
print(i_shape.tiles)
i_shape.rotate(-1)
print(i_shape.tiles)


