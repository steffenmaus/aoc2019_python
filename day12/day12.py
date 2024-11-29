import math

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_init_moons(lines):
    moons = []
    for l in lines:
        x = int(l.split('=')[1].split(',')[0])
        y = int(l.split('=')[2].split(',')[0])
        z = int(l.split('=')[3].split('>')[0])
        moons.append(((x, y, z), (0, 0, 0)))
    return moons


def f(moons):
    t = 0
    while t < 1000:
        for i1, _ in enumerate(moons):
            for i2, _ in enumerate(moons):
                if i1 > i2:
                    p1, v1 = moons[i1]
                    p2, v2 = moons[i2]
                    vx1, vy1, vz1 = v1
                    vx2, vy2, vz2 = v2
                    if p1[0] > p2[0]:
                        vx1 -= 1
                        vx2 += 1
                    elif p1[0] < p2[0]:
                        vx1 += 1
                        vx2 -= 1
                    if p1[1] > p2[1]:
                        vy1 -= 1
                        vy2 += 1
                    elif p1[1] < p2[1]:
                        vy1 += 1
                        vy2 -= 1
                    if p1[2] > p2[2]:
                        vz1 -= 1
                        vz2 += 1
                    elif p1[2] < p2[2]:
                        vz1 += 1
                        vz2 -= 1
                    moons[i1] = (p1, (vx1, vy1, vz1))
                    moons[i2] = (p2, (vx2, vy2, vz2))

        for i, m in enumerate(moons):
            p, v = m
            moons[i] = ((p[0] + v[0], p[1] + v[1], p[2] + v[2]), v)
        t += 1

    energy = 0
    for m in moons:
        p, v = m
        pot = abs(p[0]) + abs(p[1]) + abs(p[2])
        kin = abs(v[0]) + abs(v[1]) + abs(v[2])
        energy += pot * kin
    return energy


def g(moons):
    loop_per_dim = []
    for dim in range(0, 3):
        known = set()
        t = 0
        one_dim_moons = []
        for m in moons:
            one_dim_moons.append((m[0][dim], m[1][dim]))
        while True:
            if str(one_dim_moons) in known:
                loop_per_dim.append(t)
                break
            known.add(str(one_dim_moons))
            for i1, _ in enumerate(one_dim_moons):
                for i2, _ in enumerate(one_dim_moons):
                    if i1 > i2:
                        p1, v1 = one_dim_moons[i1]
                        p2, v2 = one_dim_moons[i2]
                        if p1 > p2:
                            one_dim_moons[i1] = (p1, v1 - 1)
                            one_dim_moons[i2] = (p2, v2 + 1)
                        elif p1 < p2:
                            one_dim_moons[i1] = (p1, v1 + 1)
                            one_dim_moons[i2] = (p2, v2 - 1)

            for i, m in enumerate(one_dim_moons):
                p, v = m
                one_dim_moons[i] = (p + v, v)
            t += 1
    return math.lcm(*loop_per_dim)


p1 = f(get_init_moons(lines))
print("Part 1: " + str(p1))

p2 = g(get_init_moons(lines))
print("Part 2: " + str(p2))
