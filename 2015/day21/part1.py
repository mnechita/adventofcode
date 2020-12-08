stats = open('in').read().split('\n')
bhp = int(stats[0].split(': ')[1])
bdm = int(stats[1].split(': ')[1])
bar = int(stats[2].split(': ')[1])

wep = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]
arm = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
]
rng = [
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3)
]

hp = 100
m = float('inf')


def duel(pdm, par):
    chp = hp
    cbhp = bhp
    while True:
        cbhp -= max(pdm - bar, 1)
        if cbhp <= 0:
            return True
        chp -= max(bdm - par, 1)
        if chp <= 0:
            return False


def tryall():
    global m
    rngs = [(rng[0], rng[0])] + [(rng[i], rng[j]) for i in range(len(rng)) for j in range(i+1, len(rng))]
    for w in wep:
        for a in arm:
            for r1, r2 in rngs:
                cost = w[0] + a[0] + r1[0] + r2[0]
                cur_dmg = w[1] + a[1] + r1[1] + r2[1]
                cur_arm = w[2] + a[2] + r1[2] + r2[2]
                if duel(cur_dmg, cur_arm):
                    if cost < m:
                        m = cost
    return m


print(tryall())
