from functools import reduce

data = open('in').read().split('\n\n')

ans = 0
for group in data:
    l = [set(a) for a in group.split()]
    ans += len(reduce(set.intersection, l))

print(ans)
