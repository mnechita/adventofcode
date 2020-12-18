ds = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

ds_l = ['N', 'E', 'S', 'W']
didx = 1
x = y = 0
for line in open('in').read().split('\n'):
    d = line[0]
    val = int(line[1:])
    if d == 'L':
        didx = (didx - val//90) % 4
        dx, dy = (0, 0)
    elif d == 'R':
        didx = (didx + val//90) % 4
        dx, dy = (0, 0)
    elif d == 'F':
        dx, dy = ds[ds_l[didx]]
    else:
        dx, dy = ds[d]

    x += val * dx
    y += val * dy

print(abs(x) + abs(y))
