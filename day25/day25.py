from intcodecomputer import *

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def out_as_text(out):
    lines = []
    line = ''
    for o in out:
        match o:
            case 10:
                lines.append(line)
                line = ''
            case _:
                line = line + chr(o)
    return lines


com = IntCodeComputer(lines[0])
com.run()
com.add_ascii_line("north")
com.add_ascii_line("north")
com.add_ascii_line("take astrolabe")
com.add_ascii_line("south")
com.add_ascii_line("south")
com.add_ascii_line("west")
com.add_ascii_line("north")
com.add_ascii_line("north")
com.add_ascii_line("take prime number")
com.add_ascii_line("south")
com.add_ascii_line("east")
com.add_ascii_line("take space law space brochure")
com.add_ascii_line("inv")
com.add_ascii_line("west")
com.add_ascii_line("south")
com.add_ascii_line("east")
com.add_ascii_line("south")
com.add_ascii_line("south")
com.add_ascii_line("west")
com.add_ascii_line("take mouse")
com.add_ascii_line("north")
com.add_ascii_line("north")
com.add_ascii_line("east")
com.run()

p1 = 0
for s in out_as_text(com.outputs)[-1].split():
    if s.isnumeric():
        p1 = s

print("Part 1: " + str(p1))
