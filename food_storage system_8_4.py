class addfood:
    def addfood(self):
        self.foodid=int(input("Enter food Id"))
        self.foodname=input("Enter foodname")
        self.foodtype=input("Enter food type")
        self.foodprice=float(input("Enter food price"))
class updatefood(addfood):
    def updatefood(self):
        self.foodid = int(input("Enter updated food Id"))
        self.foodname = input("Enter updated foodname")
        self.foodtype = input("Enter updated food type")
        self.foodprice = float(input("Enter updated food price"))
class showfood(updatefood):
    def showfood(self):
        print(self.foodid,self.foodname,self.foodtype,self.foodprice)
fd=showfood()
fd.addfood()
fd.updatefood()
fd.showfood()
