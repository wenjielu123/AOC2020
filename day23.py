# %%
def play(start, links, it):
    l = len(links) - 1
    current = start
    pick = [0] * 3
    dest = 0
    for _ in range(it):
        n = links[current]
        for i in range(3):
            pick[i], n = n, links[n]
        dest = ((current - 2) % l) + 1
        while dest in pick:
            dest = ((dest - 2) % l) + 1
        links[current], links[pick[2]], links[dest] = links[pick[2]], links[dest], pick[0]
        current = links[current]


# %% part 1
# input = '389125467'
input = '362981754'
input = [int(n) for n in input]

l1 = len(input)
links = [0] * (l1 + 1)
for i, n in enumerate(input):
    links[n] = input[(i+1) % l1]

play(input[0], links, 100)

lst = [0] * (l1 + 1)
n = 1
for i in range(1, (l1 + 1)):
    lst[i] = n
    n = links[n]
str1 = ''.join([str(n) for n in lst[2:]])
print(str1)

#%%
# input = '389125467'z
input = '362981754'
input = [int(n) for n in input]

l2 = 1000_000
links = [0] * (l2 + 1)

for i, n in enumerate(input):
    links[n] = input[(i+1) % l1]

for n in range(l1 + 1, l2):
    links[n] = n + 1

links[input[-1]] = l1 + 1
links[l2] = input[0]
play(input[0], links, 10000000)
val2 = links[1]
val2 *= links[val2]

print(val2)