with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def maze(p):
    return lines[p[1]][p[0]]


def get_all_nei(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def is_outter_ring(p):
    x, y = p
    return y <= 3 or y >= len(lines) - 3 or x <= 3 or x >= len(lines[3]) - 3


start = None
target = None

portals = {}
portals_lookup = {}

floor = set()
letters = set()  # not portals yet, only a single letters position

for y, _ in enumerate(lines):
    for x, _ in enumerate(lines[y]):
        c = lines[y][x]
        p = (x, y)
        if c == '.':
            floor.add(p)
        elif c.isupper():
            letters.add(p)

# each 2 letters needs to be merged to 1 portal
for l1 in letters:
    for l2 in letters:
        if l1 > l2 and l2 in get_all_nei(l1):
            id = "".join(sorted([maze(l1), maze(l2)]))
            out = None
            for f in get_all_nei(l1) + get_all_nei(l2):
                if f in floor:
                    out = f
            match id:
                case "AA":
                    start = out
                case "ZZ":
                    target = out
                case _:
                    if id in portals:
                        portals[id].append(out)
                    else:
                        portals[id] = [out]

for k in portals:
    portals_lookup[portals[k][0]] = portals[k][1]
    portals_lookup[portals[k][1]] = portals[k][0]

p1 = 0
completed = set()
open = set()
open.add(start)
while target not in open:
    p1 += 1
    next = set()
    for o in open:
        for n in get_all_nei(o):
            if n not in completed and n in floor:
                next.add(n)
        if o in portals_lookup:
            if portals_lookup[o] not in completed:
                next.add(portals_lookup[o])
        completed.add(o)
    open = next

print("Part 1: " + str(p1))

p2 = 0

completed = set()
open = set()
open.add((start, 0))
while (target, 0) not in open:
    p2 += 1
    next = set()
    for o in open:
        for n in get_all_nei(o[0]):
            if (n, o[1]) not in completed and n in floor:
                next.add((n, o[1]))
        if o[0] in portals_lookup:
            if is_outter_ring(o[0]) and o[1] > 0:
                if (portals_lookup[o[0]], o[1] - 1) not in completed:
                    next.add((portals_lookup[o[0]], o[1] - 1))
            elif not is_outter_ring(o[0]):
                if (portals_lookup[o[0]], o[1] + 1) not in completed:
                    next.add((portals_lookup[o[0]], o[1] + 1))
        completed.add(o)
    open = next

print("Part 2: " + str(p2))
