with open('in') as f:
    directions = f.read()

floor = 0

for char in directions:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
print(floor)
