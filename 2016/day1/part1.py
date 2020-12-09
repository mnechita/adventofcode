data = open('in').read().split(', ')

x = y = 0
direction = ['N', 'E', 'S', 'W']
p_dir = 0

for turn in data:
    if turn[0] == 'L':
        p_dir = (p_dir - 1) % 4
    else:
        p_dir = (p_dir + 1) % 4

    dist = int(turn[1:])

    if direction[p_dir] == 'N':
        y += dist
    elif direction[p_dir] == 'E':
        x += dist
    elif direction[p_dir] == 'S':
        y -= dist
    elif direction[p_dir] == 'W':
        x -= dist

print(abs(x) + abs(y))
