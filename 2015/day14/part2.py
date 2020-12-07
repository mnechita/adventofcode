rs = {}
for line in open('in'):
    l = line.split()
    rs[l[0]] = (int(l[3]), int(l[6]), int(l[-2]))


def compute_distance(seconds, v, t, rest):
    chunk = t + rest
    return seconds // chunk * v * t + min(seconds % chunk, t) * v


score = {}
seconds = 2503
for i in range(1, seconds + 1):
    d = {ren: compute_distance(i, v, t, rest) for ren, (v, t, rest) in rs.items()}
    _, top = max(d.items(), key=lambda x: x[1])
    for ren, v in d.items():
        if v == top:
            score[ren] = score.get(ren, 0) + 1

print(max(score.items(), key=lambda x: x[1]))
