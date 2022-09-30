numbers = open('in').read().split('\n')

digits_no = len(numbers[0])
epsilon = 0
gamma = 0
for i in range(digits_no):
    epsilon *= 2
    gamma *= 2
    ones = list(filter(lambda x: x == '1', map(lambda num: num[i], numbers)))
    if len(ones) > len(numbers) / 2:
        gamma += 1
    else:
        epsilon += 1

print(epsilon * gamma)
