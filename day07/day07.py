from intcodecomputer import *

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

import itertools

phases = range(0, 5)
p1 = 0
for p in itertools.permutations(phases):
    prev_out = 0
    for amp in p:
        temp_icc = IntCodeComputer(lines[0])
        temp_icc.add(amp)
        temp_icc.add(prev_out)
        temp_icc.run()
        prev_out = temp_icc.outputs[-1]
    p1 = max(p1, prev_out)

phases = range(5, 10)
p2 = 0
for p in itertools.permutations(phases):
    iccs = []
    for amp in p:
        temp_icc = IntCodeComputer(lines[0])
        temp_icc.add(amp)
        iccs.append(temp_icc)
    iccs[0].add(0)
    for i, ic in enumerate(iccs):
        ic.set_successor(iccs[(i + 1) % len(phases)])

    e = -1
    while e == -1:
        for ic in iccs:
            e = ic.run()

    p2 = max(p2, iccs[-1].outputs[-1])

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
