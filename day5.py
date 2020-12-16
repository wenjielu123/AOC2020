from utils import io_util

def get_pos(input, lo, hi):
    for cmd in input:
        mid = (lo + hi) // 2
        if cmd == 'F' or cmd == 'L':
            hi = mid
        elif cmd == 'B' or cmd == 'R':
            lo = mid + 1
        else:
            print(f'Invalid cmd {cmd}')
    
    assert lo == hi, "lo must equals high after the binary search"
    return lo

def get_seat(input):
    row = get_pos(input[:7], 0, 127)
    col = get_pos(input[7:], 0, 7)
    seat_id = row * 8 + col
    return row, col, seat_id

assert get_seat('BFFFBBFRRR') == (70, 7, 567)
assert get_seat('FFFBBBFRRR') == (14, 7, 119)
assert get_seat('BBFFBBFRLL') == (102, 4, 820)

inputs = io_util.read_file('inputs/day5.txt')
ids = []
for input in inputs:
    _, _, seat_id = get_seat(input)
    ids.append(seat_id)

ids.sort()
for i in range(1, len(ids) - 1):
    if ids[i] - 1 != ids[i-1]:
        print(f'{ids[i] - 1} is your seart')

    if ids[i] + 1 != ids[i+1]:
        print(f'{ids[i] + 1} is your seart')

