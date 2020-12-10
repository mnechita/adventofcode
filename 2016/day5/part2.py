from hashlib import md5

key = b'uqwqemis'

ans = [-1] * 8
i = 0
filled = 0
while filled < 8:
    hash = md5(key + str(i).encode()).hexdigest()
    if hash.startswith('00000'):
        pos = int(hash[5], 16)
        if pos < 8 and ans[pos] == -1:
            ans[pos] = hash[6]
            filled += 1
    i += 1

ans = ''.join(ans)
print(ans)
