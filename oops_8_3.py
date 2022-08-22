class pvt:
    def __init__(self):
       self.__num1=None

    def increment(self):
        a=int(input("Enter number for increment"))
        for i in range(0,a):
            i=i+1
            print("Increment ", i)
    def decrement(self):
        b=int(input("Enter number for decrement "))
        for j in range(b,0,-1):
            self.__num1=j-1
            print("decrement", self.__num1)
    def display(self):
        self.increment()
        self.decrement()

obj=pvt()
obj.increment()
obj.decrement()
obj.display()
obj1=pvt()
obj1.display()