class student:
    #Private varible
    __name=None
    __course=None
    def __init__(self):#Construct created
        print("constructor has been created")
    def __input(self):#Private method can private varible
        self.name=input("Enter Student name ")
        self.course=input("Enter the course")
    def __display(self): #Private method can private varible
        print("Student name=",self.name)
        print("Srudent course",self.course)
    def show(self):
        self.__input()
        self.__display()
    def __del__(self):
        print("Destructor has been created")
stu=student()
stu.show()



