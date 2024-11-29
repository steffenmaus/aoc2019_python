from intcodecomputer import *

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


com = IntCodeComputer(lines[0])
com.run()

scaff = set()

x = 0
y = 0
start = None
dir = None
for v in com.outputs:
    match v:
        case 10:
            x = 0
            y += 1
        case _:
            if v != ord('.'):
                scaff.add((x, y))
                if v != ord('#'):
                    dir = chr(v)
                    start = (x, y)
            x += 1

crossings = set()

for s in scaff:
    n = [n for n in get_all_nei(s) if n in scaff]
    if len(n) == 4:
        crossings.add(s)

p1 = 0
for p in crossings:
    p1 += p[0] * p[1]

print("Part 1: " + str(p1))

com = IntCodeComputer(lines[0])
com.set_mem(0, 2)

# MAIN  A B A C B C A B A C
# A     R,6,L,10,R,8,R,8
# B     R,12,L,8,L,10
# C     R,12,L,10,R,6,L,10
com.add_ascii_line("A,B,A,C,B,C,A,B,A,C")
com.add_ascii_line("R,6,L,10,R,8,R,8")
com.add_ascii_line("R,12,L,8,L,10")
com.add_ascii_line("R,12,L,10,R,6,L,10")
com.add_ascii_line("n")

com.run()

p2 = com.outputs[-1]

print("Part 2: " + str(p2))
