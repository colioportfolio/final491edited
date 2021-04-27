from parts import Wheel
from parts import Engine

class Car:
    wheelAmount = 0

    def __init__(self, shade):
        self.shade = shade
        self.name = "Wayne"
        self.speed = 0
        self.maker = "Ford"
        self.type = "Pinto"
        # self.car = Wheel(self)
        self.p = "car"


    def get_wheel_amount(self):
        wheelAmount = Wheel.amount(self.p, self.p)
        print("The Car's wheel amount is " + str(wheelAmount))
        return wheelAmount

    def owner(self):
        print(self.name + " is the owner of the " + self.p)
        return self.name

    def set_speed(self):
        self.speed = 110
        return True

    def get_speed(self):
        Car.set_speed(self)
        return self.speed

    def color(self):
        print("The color of Wayne's Ford Pinto is: " + self.shade)

    def manufacturer(self):
        print("The manufacturer of Wayne's car is " + self.maker)

    def model(self):
        print("The model of Wayne's car is a " + self.type)

    def get_engine(self):
        engineAmount = Engine.does_vehicle_have_engine(self.p, self.p)
        if engineAmount > 0:
            print("Since this is a " + self.p + ", it contains an engine")
            return engineAmount
        else:
            print("Since this is a " + self.p + ", it does not contain an engine")

    def info(self):
        self.manufacturer()
        self.model()
        self.color()
        self.owner()
        self.get_engine()
        self.get_speed()
        self.get_wheel_amount()
        print("The top speed of Wayne's " + self.maker + " " + self.type + " is " + str(self.speed) + " mph")
        return True