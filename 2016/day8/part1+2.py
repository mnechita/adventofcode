def get_column(m, col):
    res = []
    for i in range(len(m)):
        res.append(m[i][col])
    return res


width, height = 50, 6
screen = [[0] * width for _ in range(height)]
for line in open('in'):
    l = line.split()
    if l[0] == 'rect':
        wd, hg = map(int, l[1].split('x'))
        for i in range(hg):
            for j in range(wd):
                screen[i][j] = 1
    elif l[0] == 'rotate':
        cnt = int(l[-1])
        pos = int(l[2].split('=')[-1])
        if l[1] == 'row':
            cnt %= len(screen[pos])
            tmp = screen[pos] + screen[pos]
            idx = len(screen[pos]) - cnt
            screen[pos] = tmp[idx:idx+len(screen[pos])]
        elif l[1] == 'column':
            cnt %= len(screen)
            tmp = get_column(screen, pos)
            idx = len(tmp) - cnt
            tmp += tmp
            for i in range(len(screen)):
                screen[i][pos] = tmp[i+idx]

print('p1', sum(map(sum, screen)))
print('p2')
print('\n'.join([''.join(map(str, row)) for row in screen]).replace('0', ' ').replace('1', '#'))
