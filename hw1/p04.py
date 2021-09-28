def c2i(c):
    return ord(c.lower()) - 96

dollars = [1000, 500, 100, 50, 10, 1]
results = []
total = 0
base = 1
inp = input()

for i in reversed(range(3)):
    total += base * c2i(inp[i])
    base *= 26

for d in dollars:
    results.append(str(total // d))
    total = total % d

print(",".join(results))
