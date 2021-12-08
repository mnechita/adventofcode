import re


def decompress(seq):
    ans = len(seq)
    pat = re.compile(r'\((\d+)x(\d+)\)')
    last_idx = -1
    for match in pat.finditer(seq):
        if match.start() < last_idx:
            continue
        length, times = map(int, match.groups())
        ans += decompress(seq[match.end():match.end()+length]) * times - length - (match.end() - match.start())
        last_idx = match.end() + length
    return ans


inp = open('in').read()
inp = re.sub(r'\s+', '', inp)
print(decompress(inp))
