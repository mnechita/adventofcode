active = set()

for y, line in enumerate(open('in').read().split('\n')):
    for x, c in enumerate(line):
        if c == '#':
            active.add((x, y, 0, 0))


def get_active_neighbours(x, y, z, w, active_state):
    neighbours = [(i, j, k, l) for i in range(x-1, x+2) for j in range(y-1, y+2)
                  for k in range(z-1, z+2) for l in range(w-1, w+2) if (i, j, k, l) != (x, y, z, w)]
    return sum([(i, j, k, l) in active_state for (i, j, k, l) in neighbours])


for _ in range(6):
    x_min = min(active, key=lambda x: x[0])[0]
    x_max = max(active, key=lambda x: x[0])[0]
    y_min = min(active, key=lambda x: x[1])[1]
    y_max = max(active, key=lambda x: x[1])[1]
    z_min = min(active, key=lambda x: x[2])[2]
    z_max = max(active, key=lambda x: x[2])[2]
    w_min = min(active, key=lambda x: x[3])[3]
    w_max = max(active, key=lambda x: x[3])[3]

    c_active = active.copy()

    for x in range(x_min-1, x_max + 2):
        for y in range(y_min-1, y_max + 2):
            for z in range(z_min-1, z_max + 2):
                for w in range(w_min-1, w_max + 2):
                    pos = (x, y, z, w)
                    nr_active = get_active_neighbours(*pos, c_active)
                    if pos in c_active and nr_active not in {2, 3}:
                        active.remove(pos)
                    elif pos not in c_active and nr_active == 3:
                        active.add(pos)

print(len(active))
