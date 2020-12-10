from typing import Counter


lines = open('in').read().split('\n')

ans1 = ''
ans2 = ''
for i in range(len(lines[0])):
    counts = {}
    for line in lines:
        counts[line[i]] = counts.get(line[i], 0) + 1
    ans1 += max(counts, key=counts.get)
    ans2 += min(counts, key=counts.get)

print('p1', ans1)
print('p2', ans2)
