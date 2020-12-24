black = set()

for line in open('in').read().split('\n'):
    i = 0
    x = y = 0
    while i < len(line):
        c = line[i]
        if c == 'e':
            x += 2
        elif c == 'w':
            x -= 2
        else:
            i += 1
            c += line[i]
            if c == 'se':
                x += 1
                y -= 1
            elif c == 'sw':
                x -= 1
                y -= 1
            elif c == 'nw':
                x -= 1
                y += 1
            elif c == 'ne':
                x += 1
                y += 1
        i += 1
    if (x, y) in black:
        black.remove((x, y))
    else:
        black.add((x, y))

print(len(black))
