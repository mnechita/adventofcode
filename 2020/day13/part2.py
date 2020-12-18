buses = open('in').read().split('\n')[1].replace('x', '1')
buses = list(map(int, buses.split(',')))
buses = [(i, bus) for i, bus in enumerate(buses) if bus != 1]
buses = sorted(buses, key=lambda x: x[1], reverse=True)

print(buses)

inc = buses[0][1]
ans = -buses[0][0]
p = 1
while p < len(buses):
    ci, cbus = buses[p]
    ans += inc
    if (ans + ci) % cbus == 0:
        p += 1
        inc *= cbus

print(ans)
