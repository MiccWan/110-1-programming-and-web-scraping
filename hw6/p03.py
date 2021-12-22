class Student:
    def __init__(self, name, next):
        self.name = name
        self.next = next
        
    def __str__(self):
        return f'{self.name} {self.next or ""}' 
      
def remove_naughty(head, target):
    if head.name == target:
        return head.next
    else:
        cur = head
        while cur != None:
            if cur.next.name == target:
                cur.next = cur.next.next
                break
            else:
                cur = cur.next
        return head

    
# the class and function will be used as follows:
# lst = input().split()
# target = input()

# tail = Student(lst[-1], None)
# for i in range(len(lst) - 2, -1, -1):
#     head = Student(lst[i], tail)
#     tail = head
# if len(lst) == 1:
#     head = tail

# print(f'{remove_naughty(head, target) or ""}')
