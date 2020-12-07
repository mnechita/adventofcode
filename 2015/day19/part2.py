import random

rules = []
med = None
for line in open('in'):
    l = line.split()
    if len(l) == 3:
        rules.append((l[2], l[0]))
    elif len(l) == 1:
        med = l[0]

m = float('inf')
cnt = 0


def back(cur, trans):
    global m, cnt
    if cur == 'e':
        if trans < m:
            m = trans
        print('FOUND', m)
        return
    cnt += 1
    if cnt == 10000:
        cnt = 0
        print(cur, trans)
    for a, b in random.sample(rules, len(rules)):
        idx = cur.find(a)
        while idx != -1:
            back(f'{cur[:idx]}{b}{cur[idx+len(a):]}', trans+1)
            idx = cur.find(a, idx + 1)


# if answer is not found immediately, rerun
back(med, 0)
print(m)
