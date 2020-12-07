from copy import deepcopy

grid = []
grid.append([0] * 102)
for line in open('in').read().split('\n'):
    grid.append([0] + list(map(int, list(line.replace('#', '1').replace('.', '0')))) + [0])
grid.append([0] * 102)


def nrlit(m, i, j):
    part = [m[_][j-1:j+2] for _ in range(i-1, i+2)]
    return sum([sum(row) for row in part]) - m[i][j]


def switch(grid):
    old = deepcopy(grid)
    for i in range(1, 101):
        for j in range(1, 101):
            lit = nrlit(old, i, j)
            if grid[i][j] == 1 and lit not in {2, 3}:
                grid[i][j] = 0
            elif grid[i][j] == 0 and lit == 3:
                grid[i][j] = 1


for _ in range(100):
    switch(grid)

print(sum([sum(row) for row in grid]))
