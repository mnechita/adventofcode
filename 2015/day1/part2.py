with open('in') as f:
    directions = f.read()

floor = 0

for idx, char in enumerate(directions):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    if floor == -1:
        print(idx + 1)
        break
