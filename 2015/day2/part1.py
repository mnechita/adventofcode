with open('in') as f:
    dims = f.read().split('\n')

total = 0
for dim in dims:
    c_dim = sorted(list(map(int, dim.split('x'))))
    total += 3 * c_dim[0] * c_dim[1]
    total += 2 * c_dim[1] * c_dim[2]
    total += 2 * c_dim[0] * c_dim[2]

print(total)
