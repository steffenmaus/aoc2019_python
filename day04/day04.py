input = "124075-580769"

a, b = [int(x) for x in input.split('-')]


def f(n, p1):
    s = str(n)
    adj = False
    inc = True
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            if not p1:
                if i == 0 or (i > 0 and s[i - 1] != s[i]):
                    if i == len(s) - 2 or (i < len(s) - 2 and s[i] != s[i + 2]):
                        adj = True
            else:
                adj = True
        if s[i] > s[i + 1]:
            inc = False
    return adj & inc


p1 = 0
p2 = 0

for p in range(a, b):
    if f(p, True):
        p1 += 1
    if f(p, False):
        p2 += 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
