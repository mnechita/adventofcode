data = open('in').read().split('\n\n')

fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}

cnt = 0
for item in data:
    l = item.split()
    fl = set(map(lambda x: x.split(':')[0], l))
    if fl & fields == fields:
        cnt += 1
print(cnt)
