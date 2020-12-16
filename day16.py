import re
from pathlib import Path
from itertools import permutations

input_path = Path('./inputs/day16_test.txt')
# input_path = Path('./inputs/day16.txt')
with open(input_path, 'r') as f:
    inputs = f.read()

notes, my_ticket, nb_tickets = inputs.split('\n\n')
notes = notes.split('\n')
my_ticket = my_ticket.split('\n')[1:]
nb_tickets = nb_tickets.split('\n')[1:]

# print(nb_tickets)

def proc_note(notes):
    intervals = []
    intervals_notes = []
    for note in notes:
        a, b, c, d = re.findall(r'(\d+)-(\d+) or (\d+)-(\d+)', note)[0]
        a, b, c, d = map(int, (a, b, c, d))
        intervals.append((a, b))
        intervals.append((c, d))
        intervals_notes.append([(a, b), (c, d)])

    return intervals, intervals_notes

def is_valid(n, intervals):
    for a, b in intervals:
        if a <= n <= b:
            return True
    return False

def proc_nb_tickets(nb_tickets, intervals):
    valid_tickets = []
    for nb_ticket in nb_tickets:
        valid = True
        tickets = [int(t) for t in nb_ticket.split(',')]
        for ticket in tickets:
            if not is_valid(ticket, intervals):
                valid = False
                break
        if valid:
            valid_tickets.append(tickets)

    return valid_tickets

intervals, intervals_notes = proc_note(notes)
valid_tickets = proc_nb_tickets(nb_tickets, intervals)

perms = permutations(range(len(notes)))

def find_valid_fields(valid_tickets, intervals_notes):
    for perm in perms:
        valid = True
        for ticket_list in valid_tickets:
            for i, ticket in enumerate(ticket_list):
                if not (perm[i][0]<)


# find_valid_fields(valid_tickets, intervals_notes)
print(valid_tickets)