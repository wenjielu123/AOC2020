from collections import Counter, defaultdict
from utils.io_util import read_file


# input_path = 'inputs/day11_test1.txt'
input_path = 'inputs/day11.txt'

map = read_file(input_path)
nrows = len(map)
ncols = len(map[0])

def print_map(map):
    for row in map:
        print(row)

def count_adjacent_seats(map, i, j):
    occupied = 0
    for di, dj in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        if 0 <= i+di < nrows and 0 <= j+dj < ncols and map[i+di][j+dj] == '#':
            occupied += 1
    return occupied

def count_adjacent_seats_2(map, i, j):
    occupied = 0
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    for di, dj in directions:
        ii, jj = i + di, j + dj
        while 0 <= ii < nrows and 0 <= jj < ncols:
            if map[ii][jj] == '.':
                ii, jj = ii + di, jj + dj
            elif map[ii][jj] == '#':
                occupied += 1
                break
            elif map[ii][jj] == 'L':
                break
    return occupied

def sim_oneround(map):
    new_map = map.copy()
    for i in range(nrows):
        for j in range(ncols):
            if map[i][j] == 'L' and count_adjacent_seats_2(map, i, j) == 0:
                new_map[i] = new_map[i][:j] + '#' + new_map[i][j+1:]
            elif map[i][j] == '#' and count_adjacent_seats_2(map, i, j) >= 5:
                new_map[i] = new_map[i][:j] + 'L' + new_map[i][j+1:]

    return new_map

def sim_nrounds(map):
    stable = False
    counter = 0
    while not stable:
        new_map = sim_oneround(map)
        if all([new_map[i] == map[i] for i in range(nrows)]):
            print(f'Stablized at round {counter+1}!')

            n_occupied_seats = ''.join(new_map).count('#')
            print(f'Number of occupied seats = {n_occupied_seats}')
            return new_map

        map = new_map
        counter += 1
    
# new_map = sim_oneround(map)
# print_map(new_map)
sim_nrounds(map)
