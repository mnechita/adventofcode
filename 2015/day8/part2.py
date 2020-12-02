delta = 0

for line in open('in').read().split('\n'):
    delta += 2
    delta += line.count('"')
    delta += line.count('\\')
print(delta)
