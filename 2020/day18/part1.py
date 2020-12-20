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


def solve(eq):
    if eq.isnumeric():
        return int(eq)

    # solve parans
    opening_idx = eq.find('(')
    if opening_idx != -1:
        closing_idx = find_closing_paran(eq[opening_idx:]) + opening_idx
        return solve(f'{eq[:opening_idx]}{solve(eq[opening_idx+1:closing_idx])}{eq[closing_idx+1:]}')

    eq_l = eq.split()
    acc = int(eq_l[0])
    for op, val in zip(eq_l[1::2], eq_l[2::2]):
        if op == '+':
            op = add
        elif op == '*':
            op = mul
        acc = op(acc, int(val))
    return acc


ans = 0
for line in open('in').read().split('\n'):
    ans += solve(line)

print(ans)
