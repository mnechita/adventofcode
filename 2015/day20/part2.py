inp = 29000000

n = 1
while True:
    cnt = 0
    for i in range(1, int((n+1) ** 0.5)):
        if n % i != 0:
            continue
        if i * 50 >= n:
            cnt += i
        if n // i * 50 >= n:
            cnt += n // i
    cnt *= 11
    if cnt >= inp:
        break
    n += 1
    if n % 100000 == 0:
        print(n, cnt)

print(n, cnt)
