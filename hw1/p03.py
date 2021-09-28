def c2i(c):
    return ord(c.lower()) - 96

def i2c(i):
    if i == 0:
        i = 26
    return chr(i + 96)

def decode(s, k):
    s = c2i(s)
    k = c2i(k)
    if (s + k) % 2:
        return i2c(s % k)
    else:
        return i2c((s * k) % 26).upper()

cipher = input()[::-1]
key = input()

print(''.join([decode(cipher[i], key[i]) for i in range(3)]))
