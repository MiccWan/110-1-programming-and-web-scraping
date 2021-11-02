n = int(input())
all = []
all_dict = {}
whitelist = {
    "B": True,
    "R": True,
    "D": True,
    "F": True,
}

for i in range(n):
    inp = input()
    if inp.endswith("@ntu.edu.tw"):
        inp = inp[:-11]

    if len(inp) != 9:
        continue

    inp = inp[0].upper() + inp[1:]

    if not whitelist.get(inp[0]):
        continue

    if all_dict.get(inp):
        continue

    all.append(inp)
    all_dict[inp] = True

for id in all:
    print(id)
