instr = open('in').read().split('\n')


def run(reg):
    i = 0
    while 0 <= i < len(instr):
        il = instr[i].split()
        cmd = il[0]
        args = ' '.join(il[1:]).split(', ')
        if cmd == 'hlf':
            reg[args[0]] //= 2
        elif cmd == 'tpl':
            reg[args[0]] *= 3
        elif cmd == 'inc':
            reg[args[0]] += 1
        elif cmd == 'jmp':
            i += int(args[0])
            continue
        elif cmd == 'jie':
            if reg[args[0]] % 2 == 0:
                i += int(args[1])
                continue
        elif cmd == 'jio':
            if reg[args[0]] == 1:
                i += int(args[1])
                continue
        i += 1


# part 1
reg = {'a': 0, 'b': 0}
run(reg)
print(reg['b'])

# part 2
reg = {'a': 1, 'b': 0}
run(reg)
print(reg['b'])
