volts = list(map(int, open('in').read().split('\n')))

d_out = max(volts) + 3

dp = {0: 1}
for x in sorted(volts) + [d_out]:
    dp[x] = dp.get(x-3, 0) + dp.get(x-2, 0) + dp.get(x-1, 0)

print(dp[d_out])
