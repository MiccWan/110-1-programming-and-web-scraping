import re
keywords = input().split(' ')
pattern = f"({'|'.join(keywords)})"
print(pattern)
while True:
    inp = input()
    if inp == "end":
        break
    
    print(re.sub(pattern, r"「\1」", inp))