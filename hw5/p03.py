n = int(input())

vals = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
letters = ['I', 'IV', 'V', 'IX', 'X', 'XL',
           'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

index = len(vals) - 1
result = ''
while n > 0:
    if n >= vals[index]:
        n -= vals[index]
        result += letters[index]
    else:
        index -= 1

print(result)
