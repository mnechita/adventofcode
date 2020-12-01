with open('in') as f:
    words = f.read().split('\n')

nice = 0
vows = 'aeiou'
twice = [x + x for x in 'abcdefghijklmnopqrstuvwxyz']
forb = ['ab', 'cd', 'pq', 'xy']


def has3vows(word):
    vcount = 0
    for c in word:
        if c in vows:
            vcount += 1
    if vcount >= 3:
        return True
    return False


def hastwice(word):
    for x in twice:
        if x in word:
            return True
    return False


def hasforbidden(word):
    for x in forb:
        if x in word:
            return True
    return False


for word in words:
    if has3vows(word) and hastwice(word) and not hasforbidden(word):
        nice += 1
print(nice)
