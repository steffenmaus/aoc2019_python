from intcodecomputer import *

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def next_coords(x, y, dir):
    match dir % 4:
        case 0:
            y += 1
        case 1:
            x += 1
        case 2:
            y -= 1
        case 3:
            x -= 1
    return x, y


def f(p1):
    panel = {}
    if not p1:
        panel[(0, 0)] = 1
    dir = 0  # up
    x = 0
    y = 0
    c = IntCodeComputer(lines[0])
    prev_output_len = 0
    while True:
        c.add(panel.get((x, y), 0))
        c.run()
        if prev_output_len == len(c.outputs):
            break
        prev_output_len = len(c.outputs)
        painting = c.outputs[-2]
        turning = c.outputs[-1]
        panel[(x, y)] = painting
        if turning == 0:
            dir -= 1
        else:
            dir += 1
        x, y = next_coords(x, y, dir)
    return panel


panel = f(True)
p1 = len(panel.keys())
print("Part 1: " + str(p1))

panel = f(False)
xs = [c[0] for c in panel.keys()]
ys = [c[1] for c in panel.keys()]

print("Part 2:")
for y in range(max(ys), min(ys) - 1, -1):
    line = ''
    for x in range(min(xs), max(xs) + 1):
        match panel.get((x, y), 0):
            case 0:
                line = line + ' '
            case 1:
                line = line + '█'
    print(line)
