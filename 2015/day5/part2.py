with open('in') as f:
    words = f.read().split('\n')

nice = 0
alph = 'abcdefghijklmnopqrstuvwxyz'
pairs = [x + y for x in alph for y in alph]
repeats = [x + y + x for x in alph for y in alph]


def haspairtwice(word):
    for pair in pairs:
        idx = word.find(pair)
        if idx != -1:
            idx2 = word.find(pair, idx+2)
            if idx2 != -1:
                return True
    return False


def hasrepeatletter(word):
    for rep in repeats:
        if rep in word:
            return True
    return False


for word in words:
    if haspairtwice(word) and hasrepeatletter(word):
        nice += 1
print(nice)
