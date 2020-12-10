keypad = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']]
x = y = 1
ans = ''
for code in open('in').read().split('\n'):
    for c in code:
        if c == 'U':
            y = max(y - 1, 0)
        elif c == 'D':
            y = min(y + 1, 2)
        elif c == 'L':
            x = max(x - 1, 0)
        elif c == 'R':
            x = min(x + 1, 2)
    ans += keypad[y][x]

print(ans)
