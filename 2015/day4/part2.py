from hashlib import md5

key = 'ckczppom'
i = 1

while True:
    val = (key + str(i)).encode()
    hash = md5(val).hexdigest()
    if hash.startswith('000000'):
        print(i)
        break
    i += 1
