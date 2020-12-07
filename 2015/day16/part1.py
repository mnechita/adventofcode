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
    if mysue_sub == sue:
        print(i + 1)
