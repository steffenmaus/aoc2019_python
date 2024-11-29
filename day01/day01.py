with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def f1(mass):
    return mass // 3 - 2


def f2(mass):
    total = 0
    next = f1(mass)
    while next > 0:
        total += next
        next = f1(next)
    return total


p1 = sum([f1(int(l)) for l in lines])
p2 = sum([f2(int(l)) for l in lines])

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
