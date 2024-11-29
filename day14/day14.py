import math

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

rules = {}
ingredient_of = {}
ingredient_of["FUEL"] = []

for l in lines:
    left, right = l.split('=>')
    a, k = right.split()
    sources = []
    for s in left.split(','):
        temp = s.split()
        sources.append((temp[1], int(temp[0])))
        ingredient_of[temp[1]] = ingredient_of.get(temp[1], []) + [k]

    rules[k] = (int(a), sources)


def f(fuel_target):
    completed = set()
    open = set()
    open.add("FUEL")
    requirements = {}
    requirements["FUEL"] = fuel_target

    while "ORE" not in open or len(open) > 1:
        current = None
        for candidate in open:
            if all(x in completed for x in ingredient_of[candidate]):
                current = candidate

        rule = rules[current]
        mult = math.ceil(requirements[current] / rule[0])
        for t in rule[1]:
            requirements[t[0]] = requirements.get(t[0], 0) + mult * t[1]
            open.add(t[0])

        open.remove(current)
        completed.add(current)
    return requirements["ORE"]


p1 = f(1)
print("Part 1: " + str(p1))

p = 1000000000000

lower = p1
upper = p

while upper - lower > 1:
    current = (lower + upper) // 2
    res = f(current)
    if res > p:
        upper = current
    else:
        lower = current

p2 = lower
print("Part 2: " + str(p2))
