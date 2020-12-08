instr = []
for line in open('in'):
    l = line.split()
    instr.append((l[0], int(l[1])))

acc = None
ib = 0
intrerupt = True
while intrerupt:
    acc = 0
    exc = set()
    i = 0
    intrerupt = False
    while i < len(instr):
        if i in exc:
            intrerupt = True
            break
        exc.add(i)
        ci, val = instr[i]
        if ib == i and ci in {'jmp', 'nop'}:
            ci = 'jmp' if ci == 'nop' else 'nop'
        if ci == 'acc':
            acc += val
        elif ci == 'jmp':
            i += val
            continue
        i += 1
    ib += 1

print(acc)
