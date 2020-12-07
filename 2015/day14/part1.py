rs = {}
for line in open('in'):
    l = line.split()
    rs[l[0]] = (int(l[3]), int(l[6]), int(l[-2]))


def compute_distance(seconds, v, t, rest):
    chunk = t + rest
    return seconds // chunk * v * t + min(seconds % chunk, t) * v


seconds = 2503
d = [compute_distance(seconds, v, t, rest) for ren, (v, t, rest) in rs.items()]
print(max(d))
