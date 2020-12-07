inp = 29000000

n = inp // 20
isprime = [True] * n
p = 2
while p * p < n:
    if isprime[p]:
        for i in range(p * p, n, p):
            isprime[i] = False
    p += 1
primes = [i for i in range(2, n) if isprime[i]]
del isprime


def factor(n):
    fact = {}
    for p in primes:
        if n == 1:
            break
        if p * p > n:
            fact[n] = 1
            break
        while n % p == 0:
            fact[p] = fact.get(p, 0) + 1
            n //= p
    return fact


def sumdiv(n):
    s = 1
    fact = factor(n)
    for k, v in fact.items():
        s *= (k ** (v + 1) - 1) // (k - 1)
    return s


ans = 1
while True:
    cnt = 10 * sumdiv(ans)
    if cnt >= inp:
        break
    ans += 1
print(ans)
