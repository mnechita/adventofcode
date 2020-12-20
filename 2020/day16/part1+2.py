rules, mine, nearby = open('in').read().split('\n\n')
rule_d = {}
for line in rules.split('\n'):
    rule, values = line.split(': ')
    intervals = values.split(' or ')
    rule_d[rule] = []
    for interval in intervals:
        rule_d[rule].append(tuple(map(int, interval.split('-'))))


def get_candidate_rules(value):
    candidate_rules = []
    for rule, intervals in rule_d.items():
        for (l, r) in intervals:
            if l <= value <= r:
                candidate_rules.append(rule)
    return candidate_rules


nearby_m = []
ans_p1 = 0
for line in nearby.split('\n')[1:]:
    values = list(map(int, line.split(',')))
    ok = True
    for value in values:
        if len(get_candidate_rules(value)) == 0:
            ans_p1 += value
            ok = False
            break
    if ok:
        nearby_m.append(values)

print("p1", ans_p1)

cand_rules_d = {}
for i in range(len(nearby_m[0])):
    cand_rules = set(get_candidate_rules(nearby_m[0][i]))
    for line in nearby_m[1:]:
        cand_rules.intersection_update(get_candidate_rules(line[i]))
    cand_rules_d[i] = cand_rules

true_rules = {}
while cand_rules_d:
    for idx, cand_rules in cand_rules_d.copy().items():
        cand_rules_left = cand_rules - true_rules.keys()
        cand_rules_d[idx] = cand_rules_left

        if len(cand_rules_left) == 1:
            [rule] = cand_rules_left
            true_rules[rule] = idx
            del cand_rules_d[idx]
            # print(f"Found {idx}: {rule}")


mine = list(map(int, mine.split('\n')[1].split(',')))
ans_p2 = 1
for rule, idx in true_rules.items():
    if rule.startswith('departure'):
        ans_p2 *= mine[idx]

print('p2', ans_p2)
