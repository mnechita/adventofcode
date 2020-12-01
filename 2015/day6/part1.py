with open('in') as f:
    ins = f.read().split('\n')

grid = [[0] * 1000 for _ in range(1000)]


def on(x):
    return 1


def off(x):
    return 0


def tog(x):
    return 1 - x


def parse(instr):
    items = instr.split(' ')
    offset = 0
    if items[0] == 'toggle':
        op = tog
    else:
        op = on if items[1] == 'on' else off
        offset = 1
    x1, y1 = items[1 + offset].split(',')
    x2, y2 = items[-1].split(',')
    return op, int(x1), int(y1), int(x2), int(y2)


for instr in ins:
    op, x1, y1, x2, y2 = parse(instr)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] = op(grid[i][j])

print(sum([sum(row) for row in grid]))
