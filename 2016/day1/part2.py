data = open('in').read().split(', ')

x = y = 0
direction = ['N', 'E', 'S', 'W']
p_dir = 0

visited = set()
visited.add((x, y))
for turn in data:
    if turn[0] == 'L':
        p_dir = (p_dir - 1) % 4
    else:
        p_dir = (p_dir + 1) % 4

    dist = int(turn[1:])
    cx = x
    cy = y
    if direction[p_dir] == 'N':
        y += dist
    elif direction[p_dir] == 'E':
        x += dist
    elif direction[p_dir] == 'S':
        y -= dist
    elif direction[p_dir] == 'W':
        x -= dist

    skip = True
    for i in range(cx, x+1):
        for j in range(cy, y+1):
            # skip checking for start position
            if skip:
                skip = False
                continue
            if (i, j) in visited:
                print(abs(i) + abs(j))
                exit(0)
            visited.add((i, j))
