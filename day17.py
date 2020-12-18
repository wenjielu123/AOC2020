from collections import defaultdict
from utils.io_util import read_file

# input_path = 'inputs/day17_test.txt'
input_path = 'inputs/day17.txt'
inputs = read_file(input_path)

class Grid:
    def __init__(self, inputs):
        self.grid = defaultdict(int)
        self.x_min = self.x_max = 0
        self.y_min = self.y_max = 0
        self.z_min = self.w_min = 0
        self.z_max = self.w_max = 1

        self.init_grid(inputs)

    def init_grid(self, inputs):  
        """Inputs represent a 2d grid"""
        for i in range(len(inputs)):
            for j in range(len(inputs[i])):
                self.grid[(i, j, 0, 0)] = 0 if inputs[i][j] == '.' else 1
        
        self.x_max = len(inputs)
        self.y_max = len(inputs[i])
    
    def count_active(self, x, y, z, w):
        n_active = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    for dw in (-1, 0, 1):
                        x_ = x + dx
                        y_ = y + dy
                        z_ = z + dz
                        w_ = w + dw
                        if (dx,dy,dz,dw) != (0,0,0,0) and self.grid[(x_, y_, z_, w_)] == 1:
                            n_active += 1

        return n_active

    def sim_one_ground(self):
        grid_new = defaultdict(int)
        self.x_min -= 1
        self.y_min -= 1
        self.z_min -= 1
        self.w_min -= 1

        self.x_max += 1
        self.y_max += 1
        self.z_max += 1
        self.w_max += 1

        for x in range(self.x_min, self.x_max):
            for y in range(self.y_min, self.y_max):
                for z in range(self.z_min, self.z_max):
                    for w in range(self.w_min, self.w_max):
                        n_active = self.count_active(x, y, z, w)
                        if self.grid[(x,y,z,w)]:
                            if n_active == 2 or n_active == 3:
                                grid_new[(x,y,z,w)] = 1
                            else:
                                grid_new[(x,y,z,w)] = 0    
                        else:
                            if n_active == 3:
                                grid_new[(x,y,z,w)] = 1
                            else:
                                grid_new[(x,y,z,w)] = 0
        
        self.grid = grid_new

    def print_grid(self):
        for z in range(self.z_min, self.z_max):
            print(f'z = {z}')
            for x in range(self.x_min, self.x_max):
                for y in range(self.y_min, self.y_max):
                    if self.grid[(x,y,z)] == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print()

grid = Grid(inputs)
for _ in range(6):
    grid.sim_one_ground()

n_active = 0
for (x, y, z, w), active in grid.grid.items():
    n_active += active

print(n_active)