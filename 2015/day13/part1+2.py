h = {}
p = set()
for line in open('in'):
    l = line.split()
    if l[2] == 'gain':
        sgn = 1
    else:
        sgn = -1
    h[(l[0], l[-1][:-1])] = sgn * int(l[3])
    p.add(l[0])

p = sorted(list(p))


def cost(cand):
    cw = list(zip(cand, cand[1:])) + [(cand[-1], cand[0])]
    ccw = list(zip(cand[1:], cand)) + [(cand[0], cand[-1])]
    return sum(map(h.get, cw + ccw))


def search(cand, left):
    global best, m
    if len(cand) != len(p):
        for i, x in enumerate(left):
            search(cand + [x], left[:i] + left[i+1:])
    else:
        c = cost(cand)
        if c > m:
            best = cand
            m = c


# part 1
m = -float('inf')
best = None
search([p[0]], p[1:])
print(best)
print(m)

# part 2
for x in p:
    h[('me', x)] = 0
    h[(x, 'me')] = 0

p.append('me')
m = -float('inf')
best = None
search([p[0]], p[1:])
print(best)
print(m)
