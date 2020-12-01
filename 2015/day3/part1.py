with open('in') as f:
    directions = f.read()

x = y = 0
visited = {(x, y): 1}

for d in directions:
    if d == '^':
        y += 1
    elif d == 'v':
        y -= 1
    elif d == '>':
        x += 1
    elif d == '<':
        x -= 1

    visited[(x, y)] = visited.get((x, y), 0) + 1

print(len(visited))
