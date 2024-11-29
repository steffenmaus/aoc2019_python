with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

inner = {}
for l in lines:
    a, b = l.split(')')
    inner[b] = a


def f(start):
    path = set()
    current = start
    while current != "COM":
        path.add(current)
        current = inner[current]
    return path


p1 = 0
for i in inner.keys():
    p1 += len(f(i))

my_path = f("YOU")
santa_path = f("SAN")

dupl = len(my_path.intersection(santa_path))
p2 = len(my_path) + len(santa_path) - 2 * dupl - 2

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
