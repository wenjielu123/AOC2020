# %% Import data
import re
from collections import defaultdict
from utils.io_util import read_file_raw

# inputs = read_file_raw('inputs/day19_test.txt')
inputs = read_file_raw('inputs/day19.txt')
rules_raw, messages = inputs.split('\n\n')
rules_raw = rules_raw.split('\n')
messages = messages.split('\n')
verbose = False

# %% Process rules
rules = defaultdict(list)
rules_solved = defaultdict(list)
affected = set(['8', '11'])

for rule_raw in rules_raw:
    idx, rule_string = rule_raw.split(': ')
    if "\"" in rule_string:
        rules_solved[idx] = [rule_string[1:-1]]
    elif '|' in rule_string:
        rule_strings = rule_string.split(' | ')
        for r in rule_strings:
            rules[idx].append(r.split(' '))
    else:
        rules[idx].append(rule_string.split(' '))

# %% 
if verbose:
    for k, rule in rules.items():
        print(f'{k}: {rule}') 

# %% Construct the tree
def combine_two_lists_of_string(l1, l2):
    l = []
    for s1 in l1:
        for s2 in l2:
            l.append(s1 + s2)
    return l

def build_rule(rule_num):
    if rule_num in rules_solved:
        return rules_solved[rule_num]
    
    msgs = []
    for rule_set in rules[rule_num]: # e.g. rules[rule_num] = [[3,3],[4,4]]
        msgs_rule_set = ['']
        for rule in rule_set: # e.g. ruleset = ['2', '3']
            msgs_rule = build_rule(rule)
            msgs_rule_set = combine_two_lists_of_string(msgs_rule_set, msgs_rule)
            
            # Bookkeeping to avoid repetitive recursions
            if rule not in rules_solved:
                rules_solved[rule] = msgs_rule

            if rule == '8' or rule == '11' or rule_num in affected:
                affected.add(rule_num)

        for m in msgs_rule_set:
            msgs.append(m)
    
    return msgs


valid_msgs = build_rule('0')

if verbose:
    print(valid_msgs)

nvalid = 0
for msg in messages:
    if msg in valid_msgs:
        nvalid += 1

print(f'Number of valid messages = {nvalid}')
print(affected)

# %% Part 2
x42 = rules_solved['42']
x31 = rules_solved['31']

#%% Solve by recursion
len_x42 = len(x42[0])
len_x31 = len(x31[0])

def match_x11(msg):
    """Determine if a msg completely matches rule 11"""
    if len(msg) == len_x42 + len_x31:
        return msg[:len_x42] in x42 and msg[-len_x31:] in x31
    if msg == '':
        return False

    if msg[:len_x42] in x42 and msg[-len_x31:] in x31:
        return match_x11(msg[len_x42:-len_x31])
    else:
        return False

def match_rule(msg):
    if msg[:len_x42] in x42:
        return match_rule(msg[len_x42:]) or match_x11(msg)
    else:
        return match_x11(msg)

valid_msgs = []
for msg in messages:
    if msg[:len_x42] in x42 and match_rule(msg[len_x42:]):
        valid_msgs.append(msg)

print(len(valid_msgs))

#%%
