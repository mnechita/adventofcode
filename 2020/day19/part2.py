import re

rules, msgs = open('in').read().split('\n\n')

rule_d = {}
for line in rules.split('\n'):
    idx, rule = line.split(': ')
    if '"' in rule:
        rule = rule[1:-1]
    rule_d[idx] = rule

re_d = {}


def get_rule(key):
    rule = rule_d[key]
    if rule.isalpha():
        return rule
    disj = rule.split(' | ')
    res = ''
    for group in disj:
        gr_l = group.split()
        for gkey in gr_l:
            res += get_rule(gkey)
        res += '|'
    res = res[:-1]
    if len(disj) > 1:
        res = '(?:' + res + ')'
    re_d[key] = res
    return res


# Very dumb solution
rule = get_rule('0')
re_d['8'] = f"(?:{re_d['8']})+"
ans = 0
for i in range(1, 100):
    re_d['11'] = "(?:" + re_d['42'] + "{%s}" % i + re_d['31'] + "{%s}" % i + ")"
    rule = re_d['8'] + re_d['11']
    pattern = re.compile(rule)
    for msg in msgs.split('\n'):
        if pattern.fullmatch(msg) is not None:
            ans += 1
print(ans)
