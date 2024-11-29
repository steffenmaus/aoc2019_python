from intcodecomputer import *

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

c = IntCodeComputer(lines[0])
c.add(1)
c.run()

p1 = c.outputs[-1]
print("Part 1: " + str(p1))

c = IntCodeComputer(lines[0])
c.add(2)
c.run()

p2 = c.outputs[-1]
print("Part 2: " + str(p2))
