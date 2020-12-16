import re
from pathlib import Path


def read_file_by_line(input_path):
    with open(input_path, 'r') as f:
        string = f.readlines()
    
    return string

def is_valid(pwd):
    count_min, count_max, letter, pwd = re.findall(r'(\d+)-(\d+) (\w): (\w+)', pwd)[0]
    count = pwd.count(letter)

    if int(count_min) <= count <= int(count_max):
        return True
    
    return False


def is_valid2(pwd):
    pos1, pos2, letter, pwd = re.findall(r'(\d+)-(\d+) (\w): (\w+)', pwd)[0]

    if (pwd[int(pos1)-1] == letter) ^ (pwd[int(pos2)-1] == letter):
        return True
    
    return False


def part1(pwds):
    nofvalids = 0
    for pwd in pwds:
        if is_valid(pwd):
            nofvalids += 1

    return nofvalids

def part2(pwds):
    nofvalids = 0
    for pwd in pwds:
        if is_valid2(pwd):
            nofvalids += 1

    return nofvalids

# pwds = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
input_path = Path('inputs/day2.txt')
pwds = read_file_by_line(input_path)
print(part2(pwds))
