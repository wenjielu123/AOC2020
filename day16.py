import re
from pathlib import Path
from typing import DefaultDict

# input_path = Path('./inputs/day16_test.txt')
input_path = Path('./inputs/day16.txt')
with open(input_path, 'r') as f:
    inputs = f.read()

notes, my_ticket, nb_tickets = inputs.split('\n\n')
notes = notes.split('\n')
my_ticket = [int(t) for t in my_ticket.split('\n')[1].split(',')]
nb_tickets = nb_tickets.split('\n')[1:]

def proc_note(notes):
    fieldnames = []
    intervals = []
    intervals_notes = []
    for note in notes:
        fieldname, a, b, c, d = re.findall(r'([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)', note)[0]
        a, b, c, d = map(int, (a, b, c, d))
        intervals.append((a, b))
        intervals.append((c, d))
        intervals_notes.append([(a, b), (c, d)])
        fieldnames.append(fieldname)

    return fieldnames, intervals, intervals_notes

fieldnames, intervals, intervals_notes = proc_note(notes)

def is_valid(n, intervals):
    for a, b in intervals:
        if a <= n <= b:
            return True
    return False

def proc_nb_tickets(nb_tickets, intervals):
    valid_tickets = []
    err_rate = 0
    for nb_ticket in nb_tickets:
        valid = True
        tickets = [int(t) for t in nb_ticket.split(',')]
        for ticket in tickets:
            if not is_valid(ticket, intervals):
                valid = False
                err_rate += ticket
        if valid:
            valid_tickets.append(tickets)

    return valid_tickets, err_rate

valid_tickets, err_rate = proc_nb_tickets(nb_tickets, intervals)
print(err_rate)

def find_valid_pos():
    valid_positions = []
    for i, fieldname in enumerate(fieldnames): # go through each field
        intvl1, intvl2 = intervals_notes[i]
        valid_position = [[], fieldname]

        for p in range(len(fieldnames)): # go through each possible positions
            valid = True
            for ticket in valid_tickets: # e.g. ticket = [3, 9, 8]
                if not (intvl1[0] <= ticket[p] <= intvl1[1] or intvl2[0] <= ticket[p] <= intvl2[1]):
                    valid = False
                    break
            if valid:
                valid_position[0].append(p)

        valid_positions.append(valid_position)
    return valid_positions

valid_positions = sorted(find_valid_pos(), key=lambda x: len(x[0]))

def proc_valid_positions(verbose=False):
    N = len(valid_positions)
    for i in range(N):
        pos = valid_positions[i][0]
        assert len(pos) == 1
        pos_val = pos[0]

        for j in range(i+1, N):
            if pos_val in valid_positions[j][0]:
                valid_positions[j][0].remove(pos_val)

    valid_positions_dict = {}
    for valid_position in valid_positions:
        valid_positions_dict[valid_position[1]] = valid_position[0]
        if verbose:
            print(valid_position[1], ': ', valid_position[0])
    
    return valid_positions_dict

valid_positions_dict = proc_valid_positions()

def translate_my_ticket():
    my_ticket_dict = {}
    for fieldname in fieldnames:
        my_ticket_dict[fieldname] = my_ticket[valid_positions_dict[fieldname][0]]

    return my_ticket_dict

my_ticket_dict = translate_my_ticket()
# for k, v in my_ticket_dict.items():
#     print(k, ': ', v)

res = 1
for k, v in my_ticket_dict.items():
    if 'departure' in k:
        res *= v

print(res)
