g = {}

for line in open('in'):
    l = line.split()
    main_bag = ' '.join(l[:2])
    small_bags = ' '.join(l[4:])[:-1].split(', ')
    for sb in small_bags:
        sb_name = ' '.join(sb.split()[1:3])
        if sb_name not in g:
            g[sb_name] = []
        g[sb_name].append(main_bag)

visited = set()


def dfs(bag):
    cnt = 0
    if bag not in g:
        return 0
    for new_bag in g[bag]:
        if new_bag in visited:
            continue
        visited.add(new_bag)
        cnt += dfs(new_bag) + 1
    return cnt


print(dfs('shiny gold'))
