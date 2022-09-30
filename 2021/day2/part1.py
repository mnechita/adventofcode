directions = open('in').readlines()

x = 0
y = 0
for direction in directions:
    d, units = direction.split()
    units = int(units)
    if d == 'forward':
        x += units
    elif d == 'down':
        y += units
    elif d == 'up':
        y -= units

print(x * y)
