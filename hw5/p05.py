class Phonebook:
    def __init__(self):
        self.number_by_name = {}
        self.name_by_number = {}

    def search(self, name_or_number):
        code = ord(name_or_number[0])
        if 47 < code and code < 58:
            number = name_or_number
            return self.name_by_number.get(number, f"Cannot find {number}")
        else:
            name = name_or_number
            return self.number_by_name.get(name, f"Cannot find {name}")
                

    def add(self, name, number):
        self.name_by_number[number] = name
        self.number_by_name[name] = number

# # We will judge your code with the following scripts
# pbook = Phonebook()
# while True:
#     args = input().split()
#     if args[0] == "end":
#         break

#     if args[0] == "s":
#         print(pbook.search(args[1]))
#     elif args[0] == "a":
#         pbook.add(args[1], args[2])
