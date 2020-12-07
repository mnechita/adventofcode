caps = sorted(map(int, open('in').read().split('\n')))

total = 150
n = len(caps)
ans = []

K = [[float('inf') for i in range(total + 1)] for j in range(n + 1)]
cnt = [[0 for i in range(total + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, total + 1):
        K[i][w] = K[i-1][w]
        cnt[i][w] = cnt[i-1][w]
        if caps[i - 1] == w:
            if K[i][w] != 1:
                cnt[i][w] = 1
            else:
                cnt[i][w] += 1
            K[i][w] = 1
        elif caps[i - 1] < w:
            if K[i][w] > K[i-1][w - caps[i-1]] + 1:
                K[i][w] = K[i-1][w - caps[i-1]] + 1
                cnt[i][w] = cnt[i-1][w - caps[i-1]]
            elif K[i][w] == K[i-1][w - caps[i-1]] + 1:
                cnt[i][w] += cnt[i-1][w - caps[i-1]]

print(K[n][total])
print(cnt[n][total])
