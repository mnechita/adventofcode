from functools import reduce


def get_all_floating(mask):
    res = []
    current = []
    for i, c in enumerate(mask):
        if c == 'X':
            left = get_all_floating(mask[i+1:])
            res.extend([current + [0] + x for x in left])
            res.extend([current + [1] + x for x in left])
            return res
        else:
            current.append(0)
    res.append(current)
    return res


mem = {}
mask = None
mask1 = None
mask0 = None
floating_masks = None
for line in open('in').read().split('\n'):
    l = line.split(' = ')
    if l[0] == 'mask':
        mask = l[1]
        mask1 = reduce(lambda x, y: (x << 1) | y, [1 if x == '1' else 0 for x in mask], 0)
        mask0 = reduce(lambda x, y: (x << 1) | y, [0 if x == 'X' else 1 for x in mask], 1)
        floating_masks = [reduce(lambda x, y: (x << 1) | y, i, 0) for i in get_all_floating(mask)]
    else:
        addr = int(l[0].split('[')[1][:-1])
        value = int(l[1])
        addr |= mask1
        addr &= mask0
        for fmask in floating_masks:
            mem[addr | fmask] = value


print(sum(map(lambda x: x[1], mem.items())))
