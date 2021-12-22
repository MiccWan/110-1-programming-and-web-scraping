[n, m] = map(int, input().split(' '))

prices = {}
data = {}

for i in range(n):
    [item, price] = input().split(' ')
    prices[item] = int(price)

for i in range(m):
    [customer, item, amount] = input().split(' ')
    if not customer in data:
        data[customer] = {}
    data[customer][item] = data[customer].get(item, 0) + int(amount)

def A(customer):
    if not customer in data:
        return 0
    return sum([data[customer][item] * prices[item] for item in data[customer]])


def B(customer, item):
    if not customer in data:
        return 0
    return data[customer].get(item, 0)


def C(item):
    names = sorted([name for name in data if item in data[name]])
    if len(names):
        return ','.join(names)
    else:
        return 0


adapter = {
    "A": A,
    "B": B,
    "C": C,
}

while True:
    try:
        [command, *args] = input().split()
        print(adapter[command](*args))
    except:
        break
