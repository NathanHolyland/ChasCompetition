from Tetronimo import Tetronimo

class Grid:
    def __init__(self, resolution, default_color):
        self.resolution = resolution
        self.default_color = default_color
        self.grid=[]
        for i in range(resolution[0]):
            row=[]
            for j in range(resolution[1]):
                row.append(default_color)
            self.grid.append(row)
    
    def clearRow(self, row):
        empty_row = []
        for i in range(self.resolution[0]):
            empty_row.append(self.default_color)
        self.grid[row] = empty_row
        self.grid[0] = empty_row
        for i in range(row, 1, -1):
            self.grid[i] = self.grid[i-1]
    
    def clearCheck(self):
        clears = []
        for i in range(self.grid):
            full = True
            for cell in self.grid[i]:
                if cell == self.default_color:
                    full = False
            if full:
                clears.append(i)
        return clears

    def validatePosition(self, tetronimo):
        for i in tetronimo.tiles:
            x = tetronimo.position[0]+i[0]
            y = tetronimo.position[1]+i[1]
            point = [x,y]
            if point[0] < 0 or point[0] > self.resolution[0]:
                return False
            elif self.grid[x][y] != self.default_color:
                return False
        return True
    
    def changeCell(self, pos, color):
        self.grid[pos[1]][pos[0]] = color
    
    def __repr__(self):
        string = ""
        for i in self.grid:
            for j in i:
                string += f" {j} "
            string += "\n"
        return string

new_grid = Grid([10,10], 0)
for i in range(1):
    for j in range(3):
        new_grid.changeCell([7+i,7+j], 1)

new_grid.changeCell([7,8], 1)
print(new_grid)
new_grid.clearRow(9)
print(new_grid)

