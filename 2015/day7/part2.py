with open('in') as f:
    ops = f.read().split('\n')

signals = {}
values = {}


def solve(var):
    if var in values:
        return values[var]
    if var.isnumeric():
        values[var] = int(var)
    else:
        op = signals[var]
        l = op.split()
        if len(l) == 1:
            values[var] = solve(l[0])
        elif l[0] == 'NOT':
            values[var] = ~solve(l[1])
        elif l[1] == 'AND':
            values[var] = solve(l[0]) & solve(l[2])
        elif l[1] == 'OR':
            values[var] = solve(l[0]) | solve(l[2])
        elif l[1] == 'LSHIFT':
            values[var] = solve(l[0]) << solve(l[2])
        elif l[1] == 'RSHIFT':
            values[var] = solve(l[0]) >> solve(l[2])
    return values[var]


for line in ops:
    source, target = line.split(' -> ')
    signals[target] = source

a = solve('a')
values.clear()
values['b'] = a
print(solve('a'))
