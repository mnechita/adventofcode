mysue = {}
for line in open('sue').read().split('\n'):
    k, v = line.split(': ')
    mysue[k] = int(v)

sues = []
for line in open('in'):
    l = line.split()
    l = ' '.join(l[2:]).split(', ')
    sues.append({k: int(v) for k, v in map(lambda x: x.split(': '), l)})

for i, sue in enumerate(sues):
    c_keys = mysue.keys() & sue.keys()
    mysue_sub = {k: mysue[k] for k in c_keys}
    ok = True
    for k, v in mysue_sub.items():
        if k in {'cats', 'trees'}:
            if mysue_sub[k] >= sue[k]:
                ok = False
        elif k in {'pomeranians', 'goldfish'}:
            if mysue_sub[k] <= sue[k]:
                ok = False
        elif mysue_sub[k] != sue[k]:
            ok = False
    if ok:
        print(i+1)
