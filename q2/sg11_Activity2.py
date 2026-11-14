#a. Duck Typing is another programming concept to attain polymorphism besides Inheritance. The type of class is determined based on the attributes and methods it has.
#b. The child class car needs to have the same attributes as the parent class. So, the car needs to have speaks() in order to work.

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on the water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()
start_trip(car)
start_trip(boat)
start_trip(drone)

#3. The code above demonstrates polymorphism because of the duck typing concept where the function start_trip() accepts any object that has a move() method, not just its specific class.
