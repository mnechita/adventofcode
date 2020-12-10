keypad = [['0', '0', '1', '0', '0'],
          ['0', '2', '3', '4', '0'],
          ['5', '6', '7', '8', '9'],
          ['0', 'A', 'B', 'C', '0'],
          ['0', '0', 'D', '0', '0']]
lbnd = ubnd = 0
rbnd = dbnd = 4
x = 0
y = 2
ans = ''
for code in open('in').read().split('\n'):
    for c in code:
        if c == 'U':
            if y > ubnd and keypad[y-1][x] != '0':
                y -= 1
        elif c == 'D':
            if y < dbnd and keypad[y+1][x] != '0':
                y += 1
        elif c == 'L':
            if x > lbnd and keypad[y][x - 1] != '0':
                x -= 1
        elif c == 'R':
            if x < rbnd and keypad[y][x+1] != '0':
                x += 1
    ans += keypad[y][x]

print(ans)
