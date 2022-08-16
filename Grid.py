from operator import invert
from Tetronimo import Tetronimo
import pygame

def invertList(list):
    inverted = []
    for i in range(len(list[0])):
        column = []
        for j in list:
            column.append(j[i])
        inverted.append(column)
    return inverted

class Grid:
    def __init__(self, position, resolution, default_color):
        self.pos = position
        self.resolution = resolution
        self.default_color = default_color
        self.grid=[]

        #generate empty grid
        for i in range(resolution[0]):
            row=[]
            for j in range(resolution[1]):
                row.append(default_color)
            self.grid.append(row)
    
    def clearRow(self, row):
        #generate empty row
        empty_row = []
        for i in range(self.resolution[0]):
            empty_row.append(self.default_color)

        rotatedGrid = invertList(self.grid)

        #clears row, and pushes every row down and empties top row
        rotatedGrid[row] = empty_row
        for i in range(row, 1, -1):
            rotatedGrid[i] = rotatedGrid[i-1]
        rotatedGrid[0] = empty_row

        self.grid = invertList(rotatedGrid)

    
    def clearCheck(self):
        clears = []

        rotatedGrid = []
        for i in range(len(self.grid[0])):
            column = []
            for j in self.grid:
                column.append(j[i])
            rotatedGrid.append(column)
            
        #loop through each row, if the row has any blank tiles then it isnt cleared (append if it is cleared)
        for i in range(len(rotatedGrid)):
            full = True
            for cell in rotatedGrid[i]:
                if cell == self.default_color:
                    full = False
            if full:
                clears.append(i)
        return clears

    def validatePosition(self, tetronimo, input_vec):
        for i in tetronimo.tiles:
            x = int(tetronimo.position[0]+i[0] - self.pos[0])
            y = int(tetronimo.position[1]+i[1] - self.pos[0])
            point = [x,y]
            
            #if any points are out of the bounds !!not valid!!
            if point[0] < 0 or point[0] >= self.resolution[0]:
                if input_vec == [0, 1]:
                    tetronimo.activeTimer = True
                return False
            
            elif point[1] < 0 or point[1] >= self.resolution[1]:
                if input_vec == [0, 1]:
                    tetronimo.activeTimer = True
                return False
            
            #if any tiles already exist in that positon !!not valid!!
            elif self.grid[x][y] != self.default_color:
                if input_vec == [0, 1]:
                    tetronimo.activeTimer = True
                return False
        tetronimo.activeTimer = False
        return True
    
    def render(self, surface, scale):
        width = self.resolution[0]*scale[0]
        height = self.resolution[1]*scale[1]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                pygame.draw.rect(surface, self.grid[i][j], [(self.pos[0]+i)*scale[0], (self.pos[1]+j)*scale[1], scale[0], scale[1]], 0)
                if self.grid[i][j] != self.default_color:
                    pygame.draw.rect(surface, (0, 0, 0), [(self.pos[0]+i)*scale[0], (self.pos[1]+j)*scale[1], scale[0], scale[1]], 1)
        pygame.draw.rect(surface, (0,0,0), [self.pos[0]*scale[0], self.pos[1]*scale[1], width, height], 2)
        
    def changeCell(self, pos, color):
        self.grid[pos[1]][pos[0]] = color

    #find real pos of all tiles and then set the colour in the grid to that
    def commitTetronimo(self, tetronimo, grid_offset):
        for point in tetronimo.tiles:
            pos = tetronimo.position
            x = int(pos[0] + point[0] - grid_offset[0])
            y = int(pos[1] + point[1] - grid_offset[1])
            self.grid[x][y] = tetronimo.color
    
    #when the print function is called, this function will be used
    def __repr__(self):
        string = ""
        for i in self.grid:
            for j in i:
                string += f" {j} "
            string += "\n"
        return string

