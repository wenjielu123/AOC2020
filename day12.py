from os import curdir
from utils.io_util import read_file


# input_path = 'inputs/day12_test.txt'
input_path = 'inputs/day12.txt'

cmds = read_file(input_path)
directions = {0:(1, 0), 90:(0, -1), 180:(-1, 0), 270:(0, 1)}  # E, S, W, N

def read_cmd(cmd, x, y, curr_dir):
    cmd_type = cmd[0]
    cmd_num = int(cmd[1:])

    if cmd_type == "N":
        y += cmd_num
    elif cmd_type == "S":
        y -= cmd_num
    elif cmd_type == "E":
        x += cmd_num
    elif cmd_type == "W":
        x -= cmd_num
    elif cmd_type == "L":
        curr_dir = (curr_dir - cmd_num) % 360
    elif cmd_type == 'R':
        curr_dir = (curr_dir + cmd_num) % 360
    elif cmd_type == 'F':
        dx, dy = directions[curr_dir]
        x += (dx * cmd_num)
        y += (dy * cmd_num)
    else:
        raise ValueError(f'Invalid cmd {cmd_type}')

    return x, y, curr_dir

class WayPoint:
    def __init__(self):
        self.x = 10
        self.y = 1
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self, deg):  # always clockwise
        if deg == 90:
            self.x, self.y = self.y, -self.x
        elif deg == 180:
            self.x, self.y = -self.x, -self.y
        elif deg == 270:
            self.x, self.y = -self.y, self.x

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint = WayPoint()

    def forward(self, n):
        self.x += n * self.waypoint.x
        self.y += n * self.waypoint.y

def read_cmds(cmds):
    x = y = curr_dir = 0

    for cmd in cmds:
        x, y, curr_dir = read_cmd(cmd, x, y, curr_dir)

    print(abs(x)+abs(y))

def read_cmds_2(cmds):
    ship = Ship()
    for cmd in cmds:
        cmd_type = cmd[0]
        cmd_num = int(cmd[1:])
        
        if cmd_type == "N":
            ship.waypoint.y += cmd_num
        elif cmd_type == "S":
            ship.waypoint.y -= cmd_num
        elif cmd_type == "E":
            ship.waypoint.x += cmd_num
        elif cmd_type == "W":
            ship.waypoint.x -= cmd_num
        elif cmd_type == "L":
            ship.waypoint.rotate(-cmd_num % 360)
        elif cmd_type == 'R':
            ship.waypoint.rotate(cmd_num % 360)
        elif cmd_type == 'F':
            ship.forward(cmd_num)
            print(f'Ship position = ({ship.x}, {ship.y})')
        else:
            raise ValueError(f'Invalid cmd {cmd_type}')

    print(abs(ship.x) + abs(ship.y))

read_cmds_2(cmds)