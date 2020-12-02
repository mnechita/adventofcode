delta = 0

for line in open('in').read().split('\n'):
    delta += 2
    i = 0
    while i < len(line):
        chr = line[i]
        if chr == '\\':
            if line[i+1] in ['"', "\\"]:
                delta += 1
                i += 1
            elif line[i+1] == 'x':
                delta += 3
                i += 3
        i += 1
print(delta)
