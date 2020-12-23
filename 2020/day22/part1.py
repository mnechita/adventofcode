from collections import deque

p1, p2 = open('in').read().split('\n\n')
p1 = deque(map(int, p1.split('\n')[1:]))
p2 = deque(map(int, p2.split('\n')[1:]))

while len(p1) and len(p2):
    a = p1.popleft()
    b = p2.popleft()
    if a > b:
        p1.append(a)
        p1.append(b)
    else:
        p2.append(b)
        p2.append(a)

winner = p1 if len(p1) else p2

ans = sum([(len(winner) - i) * x for i, x in enumerate(winner)])
print(ans)
