with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

seed = [int(x) for x in list(lines[0])]

base_pattern = [0, 1, 0, -1]


def concat_numbers(list):
    return int("".join(str(c) for c in list))


def calc_pattern(width):
    out = []
    for e in base_pattern:
        out.extend([e] * width)
    return out


def part1(seed):
    current = seed
    for _ in range(0, 100):
        next = []
        for i, _ in enumerate(current):
            temp = 0
            pattern = calc_pattern(i + 1)
            for j, e in enumerate(current):
                mult = pattern[(j + 1) % ((i + 1) * 4)]
                temp += e * mult
            next.append(abs(temp) % 10)
        current = next
    return concat_numbers(current[:8])


def part2(seed):
    current = seed * 10000
    offset = concat_numbers(current[:7])

    current = current[offset:]
    for _ in range(0, 100):
        next = []
        last = sum(current)
        for c in current:
            next.append(last % 10)
            last -= c
        current = next

    return concat_numbers(current[:8])


p1 = part1(seed)
print("Part 1: " + str(p1))

p2 = part2(seed)
print("Part 2: " + str(p2))
