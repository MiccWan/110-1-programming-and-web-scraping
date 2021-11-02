import math

def get_base_fee(id):
    if id[0] == 'O':
        return 599
    else:
        return 699


def discount_A(inp):
    fee = sum(map(get_base_fee, inp))
    if inp[0][1] == inp[1][1] and inp[1][1] == inp[2][1]:
        fee *= 0.8
    if inp[0][0] != inp[1][0] and inp[1][0] != inp[2][0] and inp[0][0] != inp[2][0]:
        fee *= 0.8
    return math.ceil(fee - 1e-10)

def discount_B(inp):
    def discount_one(id):
        fee = get_base_fee(id)
        fee -= 70 * id.count('7')
        if (int(id[-3:]) % 7) == 0:
            fee -= 77
        return max(0, fee)
    
    return sum(map(discount_one, inp))

ids = [input(), input(), input()]

print(min(discount_A(ids), discount_B(ids)))