directions = open('in').readlines()

x = 0
y = 0
aim = 0
for direction in directions:
    d, units = direction.split()
    units = int(units)
    if d == 'forward':
        x += units
        y += aim * units
    elif d == 'down':
        aim += units
    elif d == 'up':
        aim -= units

print(x * y)
