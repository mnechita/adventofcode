def lookandsay(seq):
    prev = seq[0]
    cnt = 0
    new = ''
    for c in nr:
        if c == prev:
            cnt += 1
        else:
            new += str(cnt) + prev
            prev, cnt = c, 1
    new += str(cnt) + nr[-1]
    return new


nr = '1113222113'

for i in range(50):
    nr = lookandsay(nr)
    # part 1
    if i == 39:
        print(len(nr))

# part 2
print(len(nr))
