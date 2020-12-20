import re

rules, msgs = open('in').read().split('\n\n')

rule_d = {}
for line in rules.split('\n'):
    idx, rule = line.split(': ')
    if '"' in rule:
        rule = rule[1:-1]
    rule_d[idx] = rule


def get_rule(key):
    rule = rule_d[key]
    if rule.isalpha():
        return rule
    disj = rule.split(' | ')
    res = ''
    for group in disj:
        gr_l = group.split()
        for key in gr_l:
            res += get_rule(key)
        res += '|'
    res = res[:-1]
    if len(disj) > 1:
        res = '(?:' + res + ')'
    return res


pattern = re.compile(get_rule('0'))
ans = 0
for msg in msgs.split('\n'):
    if pattern.fullmatch(msg) is not None:
        ans += 1
print(ans)
