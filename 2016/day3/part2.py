m = []
for line in open('in'):
    m.append(list(map(int, line.split())))


def transpose(m):
    m_t = []
    for j in range(len(m[0])):
        row = []
        for i in range(len(m)):
            row.append(m[i][j])
        m_t.append(row)
    return m_t


m_t = transpose(m)
ans = 0
for line in m_t:
    for a, b, c in zip(line[::3], line[1::3], line[2::3]):
        if a + b <= c:
            continue
        if a + c <= b:
            continue
        if b + c <= a:
            continue
        ans += 1

print(ans)
