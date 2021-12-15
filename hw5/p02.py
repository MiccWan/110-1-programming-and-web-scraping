from math import factorial as f

[a, b] = map(int, input().split(' '))
[c, d] = map(int, input().split(' '))


def paths(x1, y1, x2, y2):
    return comb(x2 - x1 + y2 - y1, x2 - x1)


def comb(m, n):
    return f(m) // f(n) // f(m - n)


print(paths(0, 0, a - 1, b - 1) - paths(0, 0, c, d) * paths(c, d, a - 1, b - 1))
