from copy import deepcopy


def count_occupied_seats(seats):
    return sum([seats[i][j] == '#' for i in range(len(seats)) for j in range(len(seats[0]))])


def occupied_seats_around(seats, i, j):
    seats_around = [seats[_][max(0, j-1):min(j+2, len(seats[_]))] for _ in range(max(0, i-1), min(i+2, len(seats)))]
    return count_occupied_seats(seats_around) - (seats[i][j] == '#')


def occupy(seats):
    new = deepcopy(seats)
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == '.':
                continue
            nr_occ = occupied_seats_around(seats, i, j)
            if seats[i][j] == 'L' and nr_occ == 0:
                new[i][j] = '#'
            elif seats[i][j] == '#' and nr_occ >= 4:
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
