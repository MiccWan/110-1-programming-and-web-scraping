days = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
vac_days = {
    "AZ": 7 * 10,
    "BNT": 7 * 10,
    "moderna": 7 * 10,
    "高端": 7 * 4
}

vac_type = input()
year, month, day = map(int, input().split('/'))

to_add = vac_days[vac_type]
to_add += day

while to_add > days[month]:
    to_add -= days[month]
    month += 1

day = to_add

print(f"{year}/{month:02}/{day:02}")
