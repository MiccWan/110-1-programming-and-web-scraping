from math import factorial as f

[a, b] = map(int, input().split(' '))


def comb(m, n):
    return f(m) // f(n) // f(m - n)


print(comb(a + b - 2, a - 1))
