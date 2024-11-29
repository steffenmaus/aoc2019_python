import math

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_grid_from_lines(lines):
    rows = []
    for l in lines:
        cols = []
        for c in l:
            cols.append(c)
        rows.append(cols)
    return rows


def cart_to_rad(x, y):
    if x > 0:
        return math.atan(y / x)
    elif x < 0 and y >= 0:
        return math.atan(y / x) + math.pi
    elif x < 0 and y < 0:
        return math.atan(y / x) - math.pi
    elif x == 0 and y > 0:
        return math.pi / 2
    elif x == 0 and y < 0:
        return -math.pi / 2


grid = get_grid_from_lines(lines)
width = len(grid[0])
height = len(grid)

all = []
for x in range(width):
    for y in range(height):
        if grid[y][x] == '#':
            all.append((x, y))

best_degs = set()
best_pos = (0, 0)

for a in all:
    degs = set()
    for b in all:
        if a != b:
            dx = b[0] - a[0]
            dy = b[1] - a[1]
            degs.add(cart_to_rad(dx, dy))
    if len(degs) > len(best_degs):
        best_pos = a
        best_degs = degs

p1 = len(best_degs)
print("Part 1: " + str(p1))

ratios = list(best_degs)
ratios.sort()
top = cart_to_rad(0, -1)
pointer = 0
for k, v in enumerate(ratios):
    if v == top:
        pointer = k
        break

removals = []
remaining = set()
for a in all:
    if a != best_pos:
        dx = a[0] - best_pos[0]
        dy = a[1] - best_pos[1]
        rad = cart_to_rad(dx, dy)
        man = abs(dx) + abs(dy)
        remaining.add((man, a, rad))

while remaining:
    candidates = [r for r in remaining if r[2] == ratios[pointer]]
    if candidates:
        c = min(candidates)
        remaining.remove(c)
        removals.append(c[1])
    pointer = (pointer + 1) % len(ratios)

p2 = removals[199][0] * 100 + removals[199][1]
print("Part 2: " + str(p2))
