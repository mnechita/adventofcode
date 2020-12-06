alph = 'abcdefghjkmnpqrstuvwxyz'
inc3 = [a + b + c for a, b, c in zip(alph, alph[1:], alph[2:])]
pairs = [a + a for a in alph]


def is_valid(pasw):
    if not any([seq in pasw for seq in inc3]):
        return False

    for i, p1 in enumerate(pairs):
        idx = pasw.find(p1)
        if idx == -1:
            continue
        for p2 in pairs[:i] + pairs[i+1:]:
            if pasw[:idx].find(p2) != -1 or pasw[idx+len(p1):].find(p2) != -1:
                return True
    return False


def inc(s):
    s_l = list(s)
    for i, c in reversed(list(enumerate(s_l))):
        s_l[i] = chr(ord(c) + 1)
        if s_l[i] > 'z':
            s_l[i] = 'a'
        else:
            return ''.join(s_l)
    return 'a' + ''.join(s_l)


def next_valid(s):
    s = inc(s)
    while not is_valid(s):
        s = inc(s)
    return s


s = 'vzbxkghb'
# part 1
s = next_valid(s)
print(s)

# part 2
s = next_valid(s)
print(s)
