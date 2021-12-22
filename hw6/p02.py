class Calculator:
    def __init__(self):
        self.reset()

    def plus(self, x):
        self.record.append(self.n)
        self.n += x
        
    def minus(self, x):
        self.record.append(self.n)
        self.n -= x
        
    def multiply(self, x):
        self.record.append(self.n)
        self.n *= x
        
    def double(self):
        self.record.append(self.n)
        self.n *= 2
        
    def undo(self):
        if len(self.record):
            self.n = self.record.pop()
        
    def reset(self):
        self.record = []
        self.n = 0
        
    def show(self):
        print(self.n)


"""
We will judge your code using following scripts
"""
#my_calculator = Calculator()
#while True:
#    try:
#        cmd, *args = input().split()
#        if cmd == "plus":
#            my_calculator.plus(int(args[0]))
#        elif cmd == "minus":
#            my_calculator.minus(int(args[0]))
#        elif cmd == "multiply":
#            my_calculator.multiply(int(args[0]))
#        elif cmd == "double":
#            my_calculator.double()
#        elif cmd == "undo":
#            my_calculator.undo()
#        elif cmd == "reset":
#            my_calculator.reset()
#        elif cmd == "show":
#            my_calculator.show()
#    except:
#        break



