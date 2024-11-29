import sys

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def f(wire):
    path = {}
    x = 0
    y = 0
    steps = 0
    for e in wire.split(','):
        match e[0]:
            case 'R':
                dx = 1
                dy = 0
            case 'D':
                dx = 0
                dy = -1
            case 'L':
                dx = -1
                dy = 0
            case 'U':
                dx = 0
                dy = 1
        for _ in range(int(e[1:])):
            x += dx
            y += dy
            steps += 1
            if (x, y) not in path.keys():
                path[(x, y)] = steps
    return path


path1 = f(lines[0])
path2 = f(lines[1])

coords1 = set(path1.keys())
coords2 = set(path2.keys())

p1 = min(abs(t[0]) + abs(t[1]) for t in coords1.intersection(coords2))
print("Part 1: " + str(p1))

p2 = sys.maxsize
for c in coords1.intersection(coords2):
    a = min([path1[x] for x in coords1 if x[0] == c[0] and x[1] == c[1]])
    b = min([path2[x] for x in coords2 if x[0] == c[0] and x[1] == c[1]])
    p2 = min(p2, abs(a) + abs(b))

print("Part 2: " + str(p2))
