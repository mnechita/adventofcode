ds = {}
cs = set()
for line in open('in'):
    l = line.split()
    ds[(l[0], l[2])] = int(l[-1])
    ds[(l[2], l[0])] = int(l[-1])
    cs.add(l[0])
    cs.add(l[2])

cs = sorted(list(cs))
m = float('inf')
best = cs


def get_dist(c):
    return sum(map(ds.get, zip(c, c[1:])))


def brutesearch(cand, unvisited):
    global m, best
    cost = get_dist(cand)
    if cost > m:
        return
    if len(cand) == len(cs):
        if cost < m:
            m = cost
            best = cand
    else:
        for i, next in enumerate(unvisited):
            brutesearch(cand + [next], unvisited[:i] + unvisited[i+1:])


brutesearch([], cs)
print(best)
print(m)
