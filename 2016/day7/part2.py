import string

alph = string.ascii_lowercase
ab = [c1 + c2 for c1 in alph for c2 in alph if c1 != c2]
aba_bab = [(x + x[0], x[1] + x) for x in ab]


def find_all_occurences(substr_, str_):
    idxs = []
    idx = str_.find(substr_)
    while idx != -1:
        idxs.append(idx)
        idx = line.find(substr_, idx + len(substr_))
    return idxs


def idx_in_squared_mask(idx, brs):
    return [lb < idx < rb for lb, rb in brs]


ans = 0
for line in open('in').read().split('\n'):
    lbs = [i for i, c in enumerate(line) if c == '[']
    rbs = [i for i, c in enumerate(line) if c == ']']
    brs = list(zip(lbs, rbs))

    for aba, bab in aba_bab:
        aba_idxs = find_all_occurences(aba, line)
        bab_idxs = find_all_occurences(bab, line)
        aba_outside = any([not any(idx_in_squared_mask(idx, brs)) for idx in aba_idxs])
        bab_inside = any([any(idx_in_squared_mask(idx, brs)) for idx in bab_idxs])

        if aba_outside and bab_inside:
            ans += 1
            break

print(ans)
