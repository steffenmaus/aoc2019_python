from intcodecomputer import *

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

computers = []
output_pointers = []
for i in range(0, 50):
    com = IntCodeComputer(lines[0])
    com.add(i)
    com.add(-1)
    com.run()
    computers.append(com)
    output_pointers.append(0)

p1 = None
nat = (0, 0)
nat_prev = None
while True:
    progress = False
    for i, _ in enumerate(computers):
        new_output = computers[i].outputs[output_pointers[i]:]
        while len(new_output) > 0:
            progress = True
            output_pointers[i] += 3
            target, x, y = new_output[0:3]
            new_output = new_output[3:]
            if target == 255:
                nat = (x, y)
                if not p1:
                    p1 = y
            else:
                computers[target].add(x)
                computers[target].add(y)
        computers[i].run()
    if not progress:
        if nat_prev and nat_prev[1] == nat[1]:
            break
        nat_prev = nat
        computers[0].add(nat[0])
        computers[0].add(nat[1])
        computers[0].run()

p2 = nat_prev[1]

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
