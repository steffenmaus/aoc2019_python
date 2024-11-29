with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
with open('input2.txt') as file:
    lines2 = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def get_quadrant(p):
    x, y = p
    X = len(lines[0])
    Y = len(lines)
    if x > X // 2 and y < Y // 2:  # Topleft
        return 1
    elif x < X // 2 and y < Y // 2:  # Topright
        return 2
    elif x < X // 2 and y > Y // 2:  # Bottomleft
        return 3
    elif x > X // 2 and y > Y // 2:  # Bottomright
        return 4
    return 0


def find_blockers(maze, p, trace, req, blocked_by):
    c = maze[p[1]][p[0]]
    if c in keys.keys():
        blocked_by[c] = req
    elif c in doors.keys():
        req.add(c.lower())
    for n in get_all_nei(p):
        if n not in walls and n not in trace:
            t = trace.copy()
            t.add(p)
            find_blockers(maze, n, t, req.copy(), blocked_by)
    return blocked_by


def shortest(c, completed, open, distance, mem):
    completed.add(c)
    open.remove(c)
    if not open:
        return distance
    else:
        x = sorted(list(open))
        state = c + "".join(x)
        if state in mem:
            return distance + mem[state]
        res = []
        for o in open:
            if blocked_by[o].issubset(completed):
                res.append(shortest(o, completed.copy(), open.copy(), distance + distances[(c, o)], mem))
        mem[state] = min(res) - distance
        return min(res)


def shortest2(maze, a, b, c, d, p, completed, open, distance, mem):
    current_key = maze[p[1]][p[0]]
    completed.add(current_key)
    open.remove(current_key)
    match get_quadrant(p):
        case 1:
            a = p
        case 2:
            b = p
        case 3:
            c = p
        case 4:
            d = p
    if not open:
        return distance
    else:
        state = maze[a[1]][a[0]] + maze[b[1]][b[0]] + maze[c[1]][c[0]] + maze[d[1]][d[0]] + str(sorted(list(open)))
        if state in mem:
            return distance + mem[state]
        res = []
        for o in open:
            if blocked_by[o].issubset(completed):
                n = None
                match quads[o]:
                    case 1:
                        n = maze[a[1]][a[0]]
                    case 2:
                        n = maze[b[1]][b[0]]
                    case 3:
                        n = maze[c[1]][c[0]]
                    case 4:
                        n = maze[d[1]][d[0]]

                res.append(
                    shortest2(maze, a, b, c, d, keys[o], completed.copy(), open.copy(), distance + distances[(n, o)],
                              mem))
        mem[state] = min(res) - distance
        return min(res)


walls = set()
start = None
keys = {}
doors = {}
quads = {}  # quadrant per key

for y, _ in enumerate(lines):
    for x, _ in enumerate(lines[y]):
        c = lines[y][x]
        p = (x, y)
        match c:
            case '#':
                walls.add(p)
            case '@':
                start = p
            case _:
                if c.isupper():
                    doors[c] = p
                elif c.islower():
                    keys[c] = p
                    quads[c] = get_quadrant(p)

keys["@"] = start

# preconditions per key (keys to be found)
blocked_by = find_blockers(lines, start, set(), set(), {})

# between any keys and from start to any key
distances = {}
for k in keys.keys():
    d = 0
    x, y = keys[k]
    completed = set()
    open = set()
    open.add((x, y))
    while open:
        next = set()
        for o in open:
            for n in get_all_nei(o):
                if n not in completed and n not in walls:
                    next.add(n)
            if lines[o[1]][o[0]].islower():
                distances[(k, lines[o[1]][o[0]])] = d
            completed.add(o)
        open = next
        d += 1

p1 = shortest("@", set(), set(keys.keys()), 0, {})

print("Part 1: " + str(p1))

s1 = (start[0] + 1, start[1] - 1)  # tr
s2 = (start[0] - 1, start[1] - 1)  # tl
s3 = (start[0] - 1, start[1] + 1)  # bl
s4 = (start[0] + 1, start[1] + 1)  # br

p2 = shortest2(lines2, s1, s2, s3, s4, s1, set(), set(keys.keys()), 0, {}) - 8
print("Part 2: " + str(p2))
