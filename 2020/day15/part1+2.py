data = list(map(int, open('in').read().split(',')))
print(data)

spturn = {}
turn = 1
last = None
for nr in data:
    last = nr
    spturn[nr] = (-1, turn)
    turn += 1

while True:
    # first time spoken
    if spturn[last][0] == -1:
        if 0 not in spturn:
            spturn[0] = (-1, turn)
        else:
            spturn[0] = (spturn[0][1], turn)
        last = 0
    else:
        diff = spturn[last][1] - spturn[last][0]
        if diff not in spturn:
            spturn[diff] = (-1, turn)
        else:
            spturn[diff] = (spturn[diff][1], turn)
        last = diff
    if turn == 2020:
        print("p1", last)
    if turn == 30000000:
        print("p2", last)
        break
    turn += 1
