rules = {}
med = None
for line in open('in'):
    l = line.split()
    if len(l) == 3:
        if l[0] not in rules:
            rules[l[0]] = []
        rules[l[0]].append(l[2])
    elif len(l) == 1:
        med = l[0]

reps = set()

for a, bs in rules.items():
    idx = med.find(a, 0)
    while idx != -1:
        reps.update({med[:idx] + b + med[idx+len(a):] for b in bs})
        idx = med.find(a, idx + 1)

print(len(reps))
