class vehicle:
    spd=60
    milage=50
    def speed(self):
        print("Speed of vehicle =",self.spd)
    def mileage(self):
        print("Mileage of vehicle =", self.milage)

class car(vehicle):
    def seatcap(self,seat):
        print("seat capacity of car is ",seat)
class bus(vehicle):
    def addtionalseat(self,seat):
        print("Bus seat capacity is ",seat)

c=car()
b=bus()
c.speed()
c.mileage()
c.seatcap(5)
b.speed()
b.mileage()
b.addtionalseat(20)





