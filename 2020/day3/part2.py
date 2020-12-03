with open('in') as f:
    grid = f.read().split('\n')

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
m = len(grid[0])
ans = 1
for r, d in slopes:
    cnt = 0
    i = 0
    j = 0
    while i < len(grid):
        if grid[i][j] == '#':
            cnt += 1
        i += d
        j = (j + r) % m
    ans *= cnt

print(ans)
