from hashlib import md5

key = b'uqwqemis'

ans = []
i = 0
while len(ans) < 8:
    hash = md5(key + str(i).encode()).hexdigest()
    if hash.startswith('00000'):
        ans.append(hash[5])
    i += 1
ans = ''.join(ans)
print(ans)
