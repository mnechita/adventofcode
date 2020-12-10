ans = 0
for line in open('in'):
    a, b, c = map(int, line.split())
    if a + b <= c:
        continue
    if a + c <= b:
        continue
    if b + c <= a:
        continue
    ans += 1

print(ans)
