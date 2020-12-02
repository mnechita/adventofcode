with open('in') as f:
    lines = f.read().split('\n')

valid = 0
for line in lines:
    policy, passw = line.split(': ')
    times, char = policy.split(' ')
    minn, maxx = map(int, times.split('-'))

    if (passw[minn - 1] == char) ^ (passw[maxx - 1] == char):
        valid += 1

print(valid)
