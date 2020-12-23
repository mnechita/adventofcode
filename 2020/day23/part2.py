labels = [int(i) for i in open('in').read()]
ext = 1000000
labels.extend(range(max(labels) + 1, ext + 1))

ll = [-1] * (max(labels) + 1)
for x, y in zip(labels, labels[1:]):
    ll[x] = y
ll[labels[-1]] = labels[0]

m, M = min(labels), max(labels)
cur = labels[0]
for _ in range(10 * ext):
    first_pick = ll[cur]
    middle_pick = ll[first_pick]
    last_pick = ll[middle_pick]
    dest = cur - 1
    while dest < m or dest == first_pick or dest == middle_pick or dest == last_pick:
        if dest < m:
            dest = M
        else:
            dest -= 1
    ll[cur] = ll[last_pick]
    tmp = ll[dest]
    ll[dest] = first_pick
    ll[last_pick] = tmp
    cur = ll[cur]

print(ll[1] * ll[ll[1]])
