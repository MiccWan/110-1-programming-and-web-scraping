a = sorted(filter(lambda x: x >= 0, map(int, (input() + ' 0').split(' '))))
for i in range(len(a)):
    if i != a[i]:
        print(i)
        break
else:
    print(len(a))