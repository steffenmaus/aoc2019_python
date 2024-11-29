import random

from intcodecomputer import *

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

c = IntCodeComputer(lines[0])


def get_all_nei(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def get_next_p(p, d):
    x, y = p
    match d:
        case 1:
            return (x, y - 1)
        case 2:
            return (x, y + 1)
        case 3:
            return (x - 1, y)
        case 4:
            return (x + 1, y)


blocked = set()
empty = set()
open = set()

pos = (0, 0)
for n in get_all_nei(pos):
    open.add(n)

p1 = 0
path = []
ox = None
while open:  # improvement idea: save state of icc and reload next to unknown fields
    if pos in path:
        idx = path.index(pos)
        path = path[0:idx]
    path.append(pos)
    d = random.randint(1, 4)  # this leaves plenty of room for improvements ;)
    c.add(d)
    c.run()
    if c.outputs[-1] == 0:
        n = get_next_p(pos, d)
        blocked.add(n)
        if n in open:
            open.remove(n)
    else:
        pos = get_next_p(pos, d)
        empty.add(pos)
        if pos in open:
            open.remove(pos)
        for n in get_all_nei(pos):
            if n not in blocked and n not in empty:
                open.add(n)
        if c.outputs[-1] == 2:
            ox = pos
            p1 = len(path)

p2 = 0
floated = set()
neighbors = set()
neighbors.add(ox)
while len(floated) != len(empty):
    p2 += 1
    oldN = neighbors.copy()
    neighbors = set()
    for n in oldN:
        floated.add(n)
        newN = get_all_nei(n)
        for m in newN:
            if m not in floated and m in empty:
                neighbors.add(m)
p2 -= 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
