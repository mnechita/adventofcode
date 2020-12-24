def get_adjacent_tiles(x, y):
    return [(x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1), (x - 2, y), (x + 2, y)]


def get_nr_black_neighbours(x, y, black):
    return sum([tile in black for tile in get_adjacent_tiles(x, y)])


black = set()
white = set()
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
    cur_tile = (x, y)
    if cur_tile in black:
        black.remove(cur_tile)
        white.add(cur_tile)
    else:
        black.add(cur_tile)
        if cur_tile in white:
            white.remove(cur_tile)
        white.update([tile for tile in get_adjacent_tiles(*cur_tile)])


for day in range(100):
    white = white - black
    c_white = white.copy()
    c_black = black.copy()

    for tile in c_white:
        cnt = get_nr_black_neighbours(*tile, c_black)
        if cnt == 2:
            white.remove(tile)
            black.add(tile)
            white.update([tile for tile in get_adjacent_tiles(*tile)])
    for tile in c_black:
        cnt = get_nr_black_neighbours(*tile, c_black)
        if cnt == 0 or cnt > 2:
            white.add(tile)
            black.remove(tile)
print(len(black))
