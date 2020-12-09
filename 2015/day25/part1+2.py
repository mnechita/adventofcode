l = open('in').read().split(', ')
row = int(l[1].split()[-1])
col = int(l[2].split()[-1][:-1])
print(row, col)

prev = 20151125
grid = [[prev]]
i = 1

while True:
    if i == len(grid):
        grid.append([])
    for ci in range(i, -1, -1):
        val = (prev * 252533) % 33554393
        prev = val
        grid[ci].append(val)
        if ci + 1 == row and len(grid[ci]) == col:
            print(val)
            exit(0)
    i += 1
