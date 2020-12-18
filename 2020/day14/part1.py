from functools import reduce

mem = {}
mask = None
mask1 = None
mask0 = None
for line in open('in').read().split('\n'):
    l = line.split(' = ')
    if l[0] == 'mask':
        mask = l[1]
        mask1 = reduce(lambda x, y: (x << 1) | y, [1 if x == '1' else 0 for x in mask], 0)
        mask0 = reduce(lambda x, y: (x << 1) | y, [0 if x == '0' else 1 for x in mask], 1)
    else:
        addr = int(l[0].split('[')[1][:-1])
        value = int(l[1])
        value |= mask1
        value &= mask0
        mem[addr] = value

print(sum(map(lambda x: x[1], mem.items())))
