instr = []
for line in open('in'):
    l = line.split()
    instr.append((l[0], int(l[1])))

acc = 0
exc = set()
i = 0
while i < len(instr):
    if i in exc:
        break
    exc.add(i)
    ci, val = instr[i]
    if ci == 'acc':
        acc += val
    elif ci == 'jmp':
        i += val
        continue
    i += 1

print(acc)
