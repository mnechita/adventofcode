with open('in') as f:
    entries = [int(line) for line in f.read().split('\n')]

for i in range(len(entries)):
    for j in range(i+1, len(entries)):
        if entries[i] + entries[j] == 2020:
            print(entries[i] * entries[j])
            exit(0)
