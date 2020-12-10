import string

alph = string.ascii_lowercase
ab = [c1 + c2 for c1 in alph for c2 in alph if c1 != c2]
abba = [x + x[::-1] for x in ab]

ans = 0
for line in open('in').read().split('\n'):
    lbs = [i for i, c in enumerate(line) if c == '[']
    rbs = [i for i, c in enumerate(line) if c == ']']
    brs = list(zip(lbs, rbs))

    idxs = []
    for seq in abba:
        idx = line.find(seq)
        while idx != -1:
            idxs.append(idx)
            idx = line.find(seq, idx + len(seq))

    if not idxs:
        continue

    valid = True
    for idx in idxs:
        valid &= not any([lb < idx < rb for lb, rb in brs])
        if not valid:
            break
    if valid:
        ans += 1

print(ans)
