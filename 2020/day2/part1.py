with open('in') as f:
    lines = f.read().split('\n')

valid = 0
for line in lines:
    policy, passw = line.split(': ')
    times, char = policy.split(' ')
    minn, maxx = map(int, times.split('-'))

    cnt = 0
    for c in passw:
        if c == char:
            cnt += 1
    if minn <= cnt <= maxx:
        valid += 1

print(valid)
