eq_num = [1, 0, 9, 8, 7, 6, 5, 4, 9, 3, 2, 2,
          1, 0, 8, 9, 8, 7, 6, 5, 4, 3, 1, 3, 2, 0]
multiplier = [8, 7, 6, 5, 4, 3, 2, 1, 1]

def ID_gender(city, num):
    id = '1' + num

    check_sum = eq_num[ord(city) - 65] + sum([int(a) * b for a, b in zip(id, multiplier)])

    if check_sum % 10 == 0:
        return 'Male'
    else:
        return 'Female'

# print(ID_gender( city="A", num="87883299" ))
# print(ID_gender( city="D", num="00466791" ))