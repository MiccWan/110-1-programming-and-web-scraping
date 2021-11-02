def validate45(arr, n):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[i][j] != arr[n - 1 - j][n - 1 - i]:
                return False
    return True


def validate90(arr, m, n):
    for i in range(m):
        for j in range(n // 2):
            if arr[i][j] != arr[i][n - 1 - j]:
                return False
    return True


def validate135(arr, n):
    for i in range(1, n):
        for j in range(i):
            if arr[i][j] != arr[j][i]:
                return False
    return True


def validate0(arr, m, n):
    for i in range(m // 2):
        for j in range(n):
            if arr[i][j] != arr[m - 1 - i][j]:
                return False
    return True

def validate(arr, m, n):
    if m == n and validate135(arr, n):
        print(135)
    elif validate90(arr, m, n):
        print(90)
    elif m == n and validate45(arr, n):
        print(45)
    elif validate0(arr, m, n):
        print(0)
    else:
        print(-1)


m = int(input())
arr = []
for i in range(m):
    arr.append(list(map(int, input().split(' '))))
n = len(arr[0])
validate(arr, m, n)
