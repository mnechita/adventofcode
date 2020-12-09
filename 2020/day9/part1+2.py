data = list(map(int, open('in').read().split('\n')))


def is_sum_of(x, pre):
    s_pre = set(pre)
    for i in s_pre:
        if x - i in s_pre:
            return True
    return False


ans = None
for i, x in enumerate(data[25:], 25):
    pre = data[i-25:i]
    if not is_sum_of(x, pre):
        ans = x
        break

# part 1
print(ans)


def find_enc_weak(target):
    for i in range(len(data) - 1):
        j = i + 1
        seq = [data[i], data[j]]
        cnt = sum(seq)
        while cnt < target and j < len(data):
            j += 1
            cnt += data[j]
            seq.append(data[j])
        if cnt == target:
            return min(seq) + max(seq)


# part 2
print(find_enc_weak(ans))
