depths = list(map(int, open('in').readlines()))
depths_windows = zip(depths, depths[1:], depths[2:])
depths_windows_sum = list(map(sum, depths_windows))
prev = depths_windows_sum[0]
ans = 0
for depth in depths_windows_sum[1:]:
    if depth > prev:
        ans += 1
    prev = depth
print(ans)
