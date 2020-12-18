time, buses = open('in').read().split('\n')
time = int(time)
buses = list(map(int, filter(lambda x: x != 'x', buses.split(','))))

ctime = time - 1
ans = None
ok = False
while not ok:
    ctime += 1
    for bus in buses:
        if ctime % bus == 0:
            ans = bus
            ok = True
            break

ans *= (ctime - time)
print(ans)
