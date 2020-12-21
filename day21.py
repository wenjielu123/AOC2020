# %% Import data
import math
from collections import defaultdict
from re import match
from utils.io_util import read_file

inputs = read_file('inputs/day21_test.txt')
inputs = read_file('inputs/day21.txt')

all_ingradients = []
allergens = defaultdict(set)

# Process each line
for input in inputs:
    curr_ingradients, curr_allergens = input.split(' (')
    curr_ingradients = set(curr_ingradients.split(' '))
    curr_allergens = curr_allergens[9:-1]
    curr_allergens = set(curr_allergens.split(', '))

    all_ingradients.extend(curr_ingradients)
    for allergen in curr_allergens:
        allergens[allergen] = allergens.get(allergen, curr_ingradients).intersection(curr_ingradients)

def print_dict(d):
    for k, v in d.items():
        print(k, v)

# %% Let's identify all the allergens
allergens_identified = set()
ingradients_identified = set()
allergen_ingradient_map = {}

while len(allergens.keys()) > 0:
    for allergen, ingradients in allergens.items():
        if len(ingradients) == 1:  # identified!
            ingradient_identified = ingradients.pop()
            
            allergens_identified.add(allergen)
            ingradients_identified.add(ingradient_identified)
            allergen_ingradient_map[allergen] = ingradient_identified
        else:
            allergens[allergen] = ingradients - ingradients_identified
    
    for allergen in allergens_identified:
        if allergen in allergens:
            allergens.pop(allergen)

print_dict(allergen_ingradient_map)
# print_dict(allergens)
# print(allergens_identified)
# print(ingradients_identified)

# %% Part1 answer
ingradients_safe = set(all_ingradients) - ingradients_identified
count = 0
for ingradient in ingradients_safe:
    count += all_ingradients.count(ingradient)

print(count)

# %% Part2 answer
sorted_allergens_list = sorted(list(allergens_identified))
dangerous_ingradients = [allergen_ingradient_map[allergen] for allergen in sorted_allergens_list]
print(','.join(dangerous_ingradients))

# %%
