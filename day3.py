from pathlib import Path


def read_file_by_line(input_path):
    with open(input_path, 'r') as f:
        string = f.read().splitlines()
    
    return string

def slide(map, dy, dx):
    x = y = 0
    trees = 0

    while x < len(map) - 1:
        y = (y + dy) % len(map[x])
        x = x + dx
        
        if map[x][y] == '#':
            trees += 1

    return trees

# input_path = Path('inputs/day3_test.txt')
input_path = Path('inputs/day3.txt')

map = read_file_by_line(input_path)

trees = 1
for dy, dx in [(1,1), (3,1), (5,1), (7,1), (1, 2)]:
    trees *= slide(map, dy, dx)

print(trees) 
