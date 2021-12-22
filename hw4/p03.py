import re
from functools import reduce
import operator


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


inp = input()
inp = re.sub("[^a-zA-Z ]", "", inp)


def key1(s):
    return sum([ord(s[i]) for i in range(len(s)) if i % 2 == 0]) % 100


def key2(s):
    return sum([ord(s[i]) for i in range(len(s)) if i % 2 == 1]) % 100


def key(s):
    return (key1(s), -key2(s))


# words = list(set(inp.split(' ')))
words = inp.split(' ')
sorted_words = sorted(words, key=key)
p = prod([ord(s) - 96 for s in sorted_words[-3].lower()])
# print(sorted_words)
# print(sorted_words[-3])
# print(p)
print(str(p)[:4].zfill(4))
