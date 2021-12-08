import re

inp = open('in').read()
inp = re.sub(r'\s+', '', inp)

ans = len(inp)
pat = re.compile(r'\((\d+)x(\d+)\)')
last_idx = -1
for match in pat.finditer(inp):
    if match.start() < last_idx:
        continue
    length, times = map(int, match.groups())
    ans += length * (times-1) - (match.end() - match.start())
    last_idx = match.end() + length

print(ans)
