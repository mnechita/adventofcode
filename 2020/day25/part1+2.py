card_pub, door_pub = map(int, open('in').read().split('\n'))

subj = 7
val = 1
card_loopsz = 0
while val != card_pub:
    val = val * subj % 20201227
    card_loopsz += 1

subj = door_pub
val = 1
for _ in range(card_loopsz):
    val = val * subj % 20201227

print(val)
