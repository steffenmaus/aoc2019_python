from intcodecomputer import *

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

c = IntCodeComputer(lines[0])
c.set_mem(0,2)

p1 = -1
remaining = -1
tiles = {}
ball_x = 0
paddle_x = 0
while remaining != 0:
    tiles = {}
    c.run()
    i = 0
    while i + 2 < len(c.outputs):
        x, y, t = c.outputs[i:i + 3]
        tiles[(x, y)] = t
        if t == 3:
            paddle_x = x
        if t == 4:
            ball_x = x
        i += 3

    remaining = len([t for t in tiles.values() if t == 2])

    if p1 == -1:
        p1 = remaining

    if paddle_x > ball_x:
        c.add(-1)
    elif paddle_x < ball_x:
        c.add(1)
    else:
        c.add(0)

p2 = tiles[(-1, 0)]
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
