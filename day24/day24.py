with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

Y = len(lines)
X = len(lines[0])


def get_all_nei_2d(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def get_all_nei_3d(p):
    x, y, z = p
    r = [(x, y + 1, z), (x, y - 1, z), (x + 1, y, z), (x - 1, y, z)]
    if x == 0:
        r.append((1, 2, z - 1))
    if x == 4:
        r.append((3, 2, z - 1))
    if y == 0:
        r.append((2, 1, z - 1))
    if y == 4:
        r.append((2, 3, z - 1))

    if x == 2 and y == 1:
        r.append((0, 0, z + 1))
        r.append((1, 0, z + 1))
        r.append((2, 0, z + 1))
        r.append((3, 0, z + 1))
        r.append((4, 0, z + 1))
    if x == 2 and y == 3:
        r.append((0, 4, z + 1))
        r.append((1, 4, z + 1))
        r.append((2, 4, z + 1))
        r.append((3, 4, z + 1))
        r.append((4, 4, z + 1))
    if x == 1 and y == 2:
        r.append((0, 0, z + 1))
        r.append((0, 1, z + 1))
        r.append((0, 2, z + 1))
        r.append((0, 3, z + 1))
        r.append((0, 4, z + 1))
    if x == 3 and y == 2:
        r.append((4, 0, z + 1))
        r.append((4, 1, z + 1))
        r.append((4, 2, z + 1))
        r.append((4, 3, z + 1))
        r.append((4, 4, z + 1))
    return r


def bugs_to_string(bugs):
    return str(sorted(list(bugs)))


bugs = set()

for y, _ in enumerate(lines):
    for x, _ in enumerate(lines[0]):
        if lines[y][x] == '#':
            bugs.add((x, y))

mem = set()
while bugs_to_string(bugs) not in mem:
    mem.add(bugs_to_string(bugs))
    next_bugs = set()
    for x in range(0, X):
        for y in range(0, Y):
            if (x, y) in bugs:
                if len([n for n in get_all_nei_2d((x, y)) if n in bugs]) == 1:
                    next_bugs.add((x, y))
            else:
                if len([n for n in get_all_nei_2d((x, y)) if n in bugs]) in (1, 2):
                    next_bugs.add((x, y))
    bugs = next_bugs

p1 = sum([2 ** (b[0] + b[1] * X) for b in bugs])
print("Part 1: " + str(p1))

bugs = set()

for y, _ in enumerate(lines):
    for x, _ in enumerate(lines[0]):
        if lines[y][x] == '#':
            bugs.add((x, y, 0))

for _ in range(0, 200):
    min_z = min(b[2] for b in bugs)
    max_z = max(b[2] for b in bugs)
    next_bugs = set()
    for x in range(0, X):
        for y in range(0, Y):
            for z in range(min_z - 1, max_z + 2):
                if x != 2 or y != 2:
                    if (x, y, z) in bugs:
                        if len([n for n in get_all_nei_3d((x, y, z)) if n in bugs]) == 1:
                            next_bugs.add((x, y, z))
                    else:
                        if len([n for n in get_all_nei_3d((x, y, z)) if n in bugs]) in (1, 2):
                            next_bugs.add((x, y, z))
    bugs = next_bugs

p2 = len(bugs)
print("Part 2: " + str(p2))
