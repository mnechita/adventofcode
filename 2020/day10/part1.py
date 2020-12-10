volts = list(map(int, open('in').read().split('\n')))

prev = 0
dif1 = 0
dif3 = 0
for x in sorted(volts):
    if x - prev == 1:
        dif1 += 1
    elif x - prev == 3:
        dif3 += 1
    prev = x
dif3 += 1
print(dif1 * dif3)
