from intcodecomputer import *

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

c = IntCodeComputer(lines[0])
c.set_mem(1, 12)
c.set_mem(2, 2)
c.run()
p1 = c.get_from_mem(0)


def f(p):
    for a in range(100):
        for b in range(100):
            c = IntCodeComputer(lines[0])
            c.set_mem(1, a)
            c.set_mem(2, b)
            c.run()
            if c.get_from_mem(0) == p:
                return 100 * a + b


p2 = f(19690720)
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
