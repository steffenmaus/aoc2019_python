from intcodecomputer import *

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

p1 = 0
for y in range(0, 50):
    for x in range(0, 50):
        com = IntCodeComputer(lines[0])
        com.add(x)
        com.add(y)
        com.run()
        if com.outputs[-1]:
            p1 += 1

print("Part 1: " + str(p1))

start = {}
end = {}
start[99] = 0
end[99] = 100
for y in range(100, 2000):
    outside = True
    for x in range(start[y - 1], end[y - 1] + 3):
        com = IntCodeComputer(lines[0])
        com.add(x)
        com.add(y)
        com.run()
        if com.outputs[-1]:
            if outside:
                start[y] = x
            outside = False
        else:
            if not outside:
                end[y] = x - 1
                break
    if y - 99 in start.keys():
        if end[y - 99] >= start[y] + 99:
            break

last_y = max(start.keys())
p2 = (start[last_y] * 10000) + (last_y - 99)

print("Part 2: " + str(p2))
