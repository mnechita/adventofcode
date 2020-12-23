labels = [int(i) for i in open('in').read()]

ll = [-1] * (max(labels) + 1)
for x, y in zip(labels, labels[1:]):
    ll[x] = y
ll[labels[-1]] = labels[0]

m, M = min(labels), max(labels)
cur = labels[0]
for _ in range(100):
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

ans = [ll[1]]
for _ in range(len(labels) - 2):
    ans.append(ll[ans[-1]])

print(''.join(map(str, ans)))
