def compute_chksm(counts):
    most_com = sorted(counts, key=counts.get, reverse=True)
    ans = []
    breaks = []
    prev = -1
    last = False
    for i, c in enumerate(most_com):
        if len(ans) == 5:
            last = True
        if counts[c] != prev:
            if last:
                break
            breaks.append(i)
            prev = counts[c]
        ans.append(c)
    breaks.append(len(ans))
    for l, r in zip(breaks, breaks[1:]):
        ans = ans[:l] + sorted(ans[l:r]) + ans[r:]
    return ''.join(ans[:5])


def decrypt(enc, rot):
    return ''.join([chr(ord('a') + (ord(c) - ord('a') + rot) % 26) for c in enc])


ans1 = 0
ans2 = None
for line in open('in').read().split('\n'):
    l = line.split('-')
    enc_name = ''.join(l[:-1])
    sid, chksm = l[-1].split('[')
    sid = int(sid)
    chksm = chksm[:-1]
    counts = {}
    for c in enc_name:
        counts[c] = counts.get(c, 0) + 1
    if chksm == compute_chksm(counts):
        ans1 += sid
        if decrypt(enc_name, sid) == 'northpoleobjectstorage':
            ans2 = sid


print('p1', ans1)
print('p2', ans2)
