sugar = 0
caffeine = 0
flag = True
drink_data = {
    "M":{
        "sugar": 30,
        "caffeine":20
    },
    "B": {
        "sugar":10,
        "caffeine": 50
    }
}

for i in range(3):
    inp = input()
    drink = inp[0]
    amount = int(inp[1:])
    today_sugar = drink_data[drink]["sugar"] * amount
    today_caffeine = drink_data[drink]["caffeine"] * amount
    sugar += today_sugar
    caffeine += today_caffeine

    if today_sugar> 60 or today_caffeine>300:
        flag = False
        break

if sugar > 150 or caffeine > 700:
    flag = False

if flag:
    print("可")
else:
    print("不可")