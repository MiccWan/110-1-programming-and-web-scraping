data = {}

while True:
    inp = input()
    if inp == "end":
        break
    [phone, name, item] = inp.split(',')
    data[f'{phone[-3:]}_{name}'] = item

while True:
    try:
        inp = input()
        item = data.get(f'{inp[:3]}_{inp[4:]}', "Check again!")
        print(item)
    except:
        break