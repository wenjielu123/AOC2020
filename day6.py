from os import read
from utils.io_util import read_file_with_emptyline


def count_answers_any(input):
    answer = set()
    for line in input:
        answer = answer.union(set(line))

    return len(answer)


def count_answers_all(input):
    answer = set(input[0])
    for line in input[1:]:
        answer = answer.intersection(set(line))

    return len(answer)

def part1(inputs):
    total = 0
    for input in inputs:
        total += count_answers_any(input)
    return total

def part2(inputs):
    total = 0
    for input in inputs:
        total += count_answers_all(input)
    return total

# input_path = 'inputs/day6_test.txt'
input_path = 'inputs/day6.txt'
inputs = read_file_with_emptyline(input_path)

print(part1(inputs))
print(part2(inputs))