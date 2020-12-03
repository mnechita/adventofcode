with open('in') as f:
    grid = f.read().split('\n')

j = 0
m = len(grid[0])
cnt = 0
for line in grid:
    if line[j] == '#':
        cnt += 1
    j = (j + 3) % m

print(cnt)
