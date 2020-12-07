g = {}

for line in open('in'):
    l = line.split()
    main_bag = ' '.join(l[:2])
    small_bags = ' '.join(l[4:])[:-1].split(', ')
    if main_bag not in g:
        g[main_bag] = []
    g[main_bag].extend([(int(sb[0].replace('no', '0')), ' '.join(sb[1:3]))
                        for sb in map(lambda x: x.split(), small_bags)])

visited = {}


def dfs(qty, bag):
    cnt = 0
    if qty == 0:
        return 0
    for new_qty, new_bag in g[bag]:
        if new_bag in visited:
            cnt += new_qty + new_qty * visited[new_bag]
            continue
        cnt += new_qty + dfs(new_qty, new_bag)
    visited[bag] = cnt
    return qty * cnt


print(dfs(1, 'shiny gold'))
