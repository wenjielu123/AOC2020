import re
from collections import OrderedDict
from utils.io_util import read_file

class Bag:
    def __init__(self, color):
        self.color = color
        self.subbags = []
    
    def add_bag(self, quantity, bag):
        self.subbags.append((bag, quantity))

    def __str__(self):
        res = f'{self.color} -> '
        for bag, quantity in self.subbags:
            res += f'{quantity} {bag.color}, '
        return res

def dfs(root:Bag):
    visited = []
    total = dfs_helper(root, visited) - 1
    return visited, total

def dfs_helper(node, visited):
    if not node.subbags:
        return 1

    total = 0
    for subbag, quantity in node.subbags:
        # if subbag.color not in visited:
        visited.append(subbag.color)
        total += quantity * dfs_helper(subbag, visited)
    
    return total + 1
    
def parse_line(line):
    bag, leaves = line.split(' bags contain ')
    if 'no other bags' in leaves:
        return bag, []
    
    leaves = leaves.split(', ')
    sub_bags = []
    for leaf in leaves:
        n, color = re.findall(r'(\d+)\s([\w\s]+)\sbag', leaf)[0]
        sub_bags.append((int(n), color))
    
    return bag, sub_bags

def parse_inputs(inputs):
    bags = OrderedDict()

    for line in inputs:
        bag_color, subbags = parse_line(line)
        if bag_color not in bags:
            bag = Bag(bag_color)
            bags[bag_color] = bag
        else:
            bag = bags[bag_color]

        for quantity, subbag_color in subbags:
            if subbag_color not in bags:  # meet a new type of bag
                subbag = Bag(subbag_color)
                bags[subbag_color] = subbag
            else:
                subbag = bags[subbag_color]
            
            bag.add_bag(quantity, subbag)
    
    return bags

# input_path = 'inputs/day7_test2.txt'
input_path = 'inputs/day7.txt'
inputs = read_file(input_path)
bags = parse_inputs(inputs)

def part1():
    count = 0
    for _, bag in bags.items():
        count += 'shiny gold' in dfs(bag)

    print(count)

# part1()

def part2():
    # _, total = dfs(bags['vibrant plum'])
    _, total = dfs(bags['shiny gold'])
    print(total)

part2()