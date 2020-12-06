data = open('in').read().split('\n\n')

ans = 0
for group in data:
    ans += len(set(''.join(group.split())))

print(ans)
