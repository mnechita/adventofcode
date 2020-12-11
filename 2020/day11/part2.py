from copy import deepcopy


def count_occupied_seats(seats):
    return sum([seats[i][j] == '#' for i in range(len(seats)) for j in range(len(seats[0]))])


def occupied_seats_around(seats, i, j):
    dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    cnt = 0
    for di, dj in dirs:
        ci = i + di
        cj = j + dj
        while 0 <= ci < len(seats) and 0 <= cj < len(seats[ci]) and seats[ci][cj] == '.':
            ci += di
            cj += dj
        if not (0 <= ci < len(seats) and 0 <= cj < len(seats[ci])):
            continue
        if seats[ci][cj] == '#':
            cnt += 1
    return cnt


def occupy(seats):
    new = deepcopy(seats)
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == '.':
                continue
            nr_occ = occupied_seats_around(seats, i, j)
            if seats[i][j] == 'L' and nr_occ == 0:
                new[i][j] = '#'
            elif seats[i][j] == '#' and nr_occ >= 5:
                new[i][j] = 'L'
    return new


def pp(m):
    print('\n'.join([''.join(row) for row in m]))


layout = list(map(list, open('in').read().split('\n')))

prev = None
while layout != prev:
    prev = layout
    layout = occupy(prev)

print(count_occupied_seats(layout))
