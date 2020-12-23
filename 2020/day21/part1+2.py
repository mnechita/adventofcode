from functools import reduce

all_ings = set()
alergens = {}
food_ing_l = []
for line in open('in').read().split('\n'):
    ings, alergs = line.split(' (contains ')
    alergs = alergs[:-1].split(', ')
    ings = ings.split()
    food_ing_l.append(set(ings))
    all_ings.update(ings)
    for alerg in alergs:
        if alerg not in alergens:
            alergens[alerg] = set(ings)
        else:
            alergens[alerg].intersection_update(ings)

suspicious = reduce(set.union, [v for k, v in alergens.items()])
p1_ans = 0
for ing in all_ings - suspicious:
    for food_ing in food_ing_l:
        if ing in food_ing:
            p1_ans += 1
print('p1', p1_ans)

confirmed = set()
ok = False
while not ok:
    ok = True
    for alerg, ings in alergens.copy().items():
        if len(ings) == 1:
            confirmed.update(ings)
        else:
            ok = False
            alergens[alerg] = ings - confirmed

print('p2', ''.join(map(lambda x: list(x[1])[0], sorted(alergens.items()))))
