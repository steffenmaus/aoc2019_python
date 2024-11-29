with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

current = [x for x in range(0, 10007)]

for l in lines:
    if l == 'deal into new stack':
        current.reverse()
    elif l.startswith('cut '):
        pos = int(l.split()[-1])
        current = current[pos:] + current[:pos]
    elif l.startswith('deal with increment '):
        inc = int(l.split()[-1])
        temp = current.copy()
        for i, _ in enumerate(temp):
            current[(i * inc) % len(temp)] = temp[i]

p1 = current.index(2019)

cards_total = 119315717514047
N = 101741582076661


# mod inverse for p prime:
# inv = x^(p-2) mod p
def mod_inv(a, p):
    return pow(a, p - 2, p)


pos = 2020
# lin alg
# y = ax + b

# y1 = (ax + b) % p
# y2 = (aax + ab + b) % p
#   == (aax + (a+1)b) % p
# yN = (a^N * x + (a^N-1 + .. + a^1 + a^0)b) % p
#   == (a^N * x + ((a^N - 1) / a-1)b) % p #?!?!?!??!
#   == (a^N * x + ((a^N - 1) * mod_inv(a-1))b) % p
m = 1
n = 0
for l in reversed(lines):
    if l == 'deal into new stack':
        pos = cards_total - 1 - pos
        m = -m
        n = -n - 1
    elif l.startswith('cut '):
        shift = int(l.split()[-1])
        pos += shift
        n += shift
    elif l.startswith('deal with increment '):
        inc = int(l.split()[-1])
        pos = pos * mod_inv(inc, cards_total)
        m *= mod_inv(inc, cards_total)
        n *= mod_inv(inc, cards_total)

    pos %= cards_total
    m %= cards_total
    n %= cards_total

pos = 2020
y_high = (pow(m, N, cards_total) * pos + ((pow(m, N, cards_total) - 1) * mod_inv(m - 1, cards_total)) * n) % cards_total
p2 = y_high

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
