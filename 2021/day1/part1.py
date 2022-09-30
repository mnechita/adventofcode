depths = list(map(int, open('in').readlines()))
prev = depths[0]
ans = 0
for depth in depths[1:]:
    if depth > prev:
        ans += 1
    prev = depth
print(ans)
