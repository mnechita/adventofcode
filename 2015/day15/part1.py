from functools import reduce

ing = {}
for line in open('in'):
    l = line.split()
    ing[l[0][:-1]] = {
        'cap': int(l[2][:-1]),
        'dur': int(l[4][:-1]),
        'fla': int(l[6][:-1]),
        'tex': int(l[8][:-1]),
        'cal': int(l[10]),
    }
ing_names = sorted(ing.keys())


def score(cand):
    cap = dur = fla = tex = cal = 0
    for i, cnt in cand.items():
        cap += ing[i]['cap'] * cnt
        dur += ing[i]['dur'] * cnt
        fla += ing[i]['fla'] * cnt
        tex += ing[i]['tex'] * cnt
        cal += ing[i]['cal'] * cnt
    stats = [cap, dur, fla, tex]
    if all([s > 0 for s in stats]):
        return reduce(lambda x, y: x * y, stats)
    return 0


i = 0
M = 0
best = None

for s in range(101):
    for b in range(101 - s):
        for ch in range(101 - s - b):
            cand = {
                'Sprinkles': s,
                'Butterscotch': b,
                'Chocolate': ch,
                'Candy': 100 - s - b - ch
            }
            sc = score(cand)
            if sc > M:
                M = sc
                best = cand

print(best)
print(M)
