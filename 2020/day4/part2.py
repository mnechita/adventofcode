import re

data = open('in').read().split('\n\n')


def val_hgt(x):
    try:
        m = x[-2:]
        val = int(x[:-2])
        if m == 'in':
            return 59 <= val <= 76
        elif m == 'cm':
            return 150 <= val <= 193
        return False
    except:
        return False


fields = {
    'byr': lambda x: len(x) == 4 and x.isnumeric() and 1920 <= int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and x.isnumeric() and 2010 <= int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and x.isnumeric() and 2020 <= int(x) <= 2030,
    "hgt": val_hgt,
    "hcl": lambda x: re.match(r'^#[0-9a-f]{6}$', x),
    "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda x: re.match(r'^[0-9]{9}$', x),
}

cnt = 0
for item in data:
    l = item.split()
    fl = {k: v for k, v in map(lambda x: x.split(':'), l)}

    if (fl.keys() & fields.keys()) == fields.keys():
        ok = True
        for k, val in fields.items():
            if not val(fl[k]):
                ok = False
                break
        if ok:
            cnt += 1
print(cnt)
