import datetime



class employee:
    def __init__ (self):
        self.name = input("Enter name of Emp")
        self.birthyear = int(input("Enter Birth year of emp"))
    def age(self):
        x = datetime.datetime.now()
        z=x.year

        print("Name of employee=",self.name)
        print("Age of employee=",z-self.birthyear)
new_emp=employee()
new_emp.age()


