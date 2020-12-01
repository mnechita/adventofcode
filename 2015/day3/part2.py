with open('in') as f:
    directions = f.read()

xs = ys = xr = yr = 0
visited = {(xs, ys): 2}


def next_house(x, y, d):
    if d == '^':
        y += 1
    elif d == 'v':
        y -= 1
    elif d == '>':
        x += 1
    elif d == '<':
        x -= 1
    return x, y


for i in range(0, len(directions), 2):
    xs, ys = next_house(xs, ys, directions[i])
    visited[(xs, ys)] = visited.get((xs, ys), 0) + 1

for i in range(1, len(directions), 2):
    xr, yr = next_house(xr, yr, directions[i])
    visited[(xr, yr)] = visited.get((xr, yr), 0) + 1

print(len(visited))
