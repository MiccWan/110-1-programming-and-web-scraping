height = int(input())
width = int(input())


def makeGenerator(items):
    i = 0
    while True:
        yield items[i]
        i = (i+1) % len(items)

num_gen = makeGenerator('1234567890')
cap_gen = makeGenerator('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lit_gen = makeGenerator('abcdefghijklmnopqrstuvwxyz')

for i in range(height):
    if i % 3 == 0:
        cur_gen = cap_gen
    elif i % 3 == 1:
        cur_gen = lit_gen
    else:
        cur_gen = num_gen
    for j in range(width + i):
        print(next(cur_gen), end="")
    print('')
