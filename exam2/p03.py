n = int(input())
d = int(input())
m = int(input())
available_cars = list(map(int, input().split(' ')))
available_rooms = list(map(int, input().split(' ')))
budget = int(input())
room_prices = list(map(int, input().split(' ')))

cars_needed = -(n // -5)
rooms_needed = -(n // -4)
for i in range(len(available_cars) - d + 1):
    if not all([cars_needed <= x for x in available_cars[i:i+d]]):
        continue
    if not all([rooms_needed <= x for x in available_rooms[i:(i+d-1)]]):
        continue
    if not budget >= sum(room_prices[i:(i+d-1)])*rooms_needed:
        continue
    print(i+1)
    break
else:
    print(None)


# print(n, d, m, budget, cars_needed, rooms_needed)
# print(available_cars)
# print(available_rooms)
# print(room_prices)
