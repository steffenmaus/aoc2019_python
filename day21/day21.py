from intcodecomputer import *

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def f(p1):
    com = IntCodeComputer(lines[0])
    com.add_ascii_line("NOT A J")  # jump if gap at a
    com.add_ascii_line("NOT B T")
    com.add_ascii_line("OR T J")  # jump if gap at a or b
    com.add_ascii_line("NOT C T")
    com.add_ascii_line("OR T J")  # jump if gap at a,b or c
    com.add_ascii_line("NOT D T")
    com.add_ascii_line("NOT T T")
    com.add_ascii_line("AND T J")  # jump if (gap at a,b or c) AND (hull at d)

    if not p1:
        com.add_ascii_line("NOT H T")
        com.add_ascii_line("NOT T T")
        com.add_ascii_line("OR E T")
        com.add_ascii_line("AND T J")  # jump if (gap at a,b or c) AND (hull at d) AND (hull at h or e)
        com.add_ascii_line("RUN")
    else:
        com.add_ascii_line("WALK")

    com.run()

    return com.outputs[-1]


p1 = f(True)
p2 = f(False)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
