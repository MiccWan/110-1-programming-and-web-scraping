class Student:
    def __init__(self, name, next):
        self.name = name
        self.next = next
        
    def __str__(self):
        return f'{self.name} {self.next or ""}' 
      
def reverse_students(head):
    queue = [None]
    cur = head
    while cur != None:
        queue.append(cur)
        cur = cur.next

    for i in range(len(queue) - 1, 0, -1):
        queue[i].next = queue[i - 1]

    return queue[-1]
    
# the class and function will be used as follows:
# lst = input().split()

# tail = Student(lst[-1], None)
# for i in range(len(lst) - 2, -1, -1):
#     head = Student(lst[i], tail)
#     tail = head
# if len(lst) == 1:
#     head = tail

# print(f'{reverse_students(head) or ""}')
