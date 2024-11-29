import sys

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def grouped(list, group_size):
    lists = []
    for i in range(0, len(list), group_size):
        lists.append(list[i:i + group_size])
    return lists


wide = 25
tall = 6

layers = grouped(lines[0], tall * wide)

temp = (sys.maxsize, 0)
for l in layers:
    if l.count('0') < temp[0]:
        temp = (l.count('0'), l.count('1') * (l.count('2')))

p1 = temp[1]
print("Part 1: " + str(p1))

print("Part 2:")
line = ''
for i in range(wide * tall):
    for l in layers:
        if l[i] == '0':
            line += ' '
            break
        elif l[i] == '1':
            line += '█'
            break
    if (i + 1) % wide == 0:
        print(line)
        line = ''
