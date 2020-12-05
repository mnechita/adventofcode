data = open('in').read().split('\n')
data = [int(x.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for x in data]

print(set(range(min(data), max(data) + 1)) - set(data))
