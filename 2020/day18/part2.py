from operator import add, mul


def find_closing_paran(eq):
    cnt = 0
    for i, c in enumerate(eq):
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        if cnt == 0:
            return i


def compute_order(eq_l):
    if len(eq_l) == 1:
        return int(eq_l[0])
    for i, c in enumerate(eq_l):
        if c == '+':
            return compute_order(eq_l[:i-1] + [int(eq_l[i-1]) + int(eq_l[i + 1])] + eq_l[i+2:])
    for i, c in enumerate(eq_l):
        if c == '*':
            return compute_order(eq_l[:i-1] + [int(eq_l[i-1]) * int(eq_l[i + 1])] + eq_l[i+2:])


def solve(eq):
    if eq.isnumeric():
        return int(eq)

    # solve parans
    opening_idx = eq.find('(')
    if opening_idx != -1:
        closing_idx = find_closing_paran(eq[opening_idx:]) + opening_idx
        return solve(f'{eq[:opening_idx]}{solve(eq[opening_idx+1:closing_idx])}{eq[closing_idx+1:]}')

    return compute_order(eq.split(' '))


ans = 0
for line in open('in').read().split('\n'):
    ans += solve(line)

print(ans)
