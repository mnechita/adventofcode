from collections import deque
from itertools import islice

p1, p2 = open('in').read().split('\n\n')
p1 = deque(map(int, p1.split('\n')[1:]))
p2 = deque(map(int, p2.split('\n')[1:]))


def combat(p1, p2):
    rounds = set()
    while len(p1) and len(p2):
        config = (tuple(p1), tuple(p2))
        if config in rounds:
            return 1
        else:
            rounds.add(config)

        a = p1.popleft()
        b = p2.popleft()
        if a <= len(p1) and b <= len(p2):
            winner = combat(deque(islice(p1, 0, a)), deque(islice(p2, 0, b)))
            if winner == 1:
                p1.append(a)
                p1.append(b)
            else:
                p2.append(b)
                p2.append(a)
        else:
            if a > b:
                p1.append(a)
                p1.append(b)
            else:
                p2.append(b)
                p2.append(a)
    return 1 if len(p1) else 2


combat(p1, p2)
winner = p1 if len(p1) else p2

ans = sum([(len(winner) - i) * x for i, x in enumerate(winner)])
print(ans)
