from parts import Wheel
from parts import Engine
class Bike:
    def __init__(self, shade, type):
        self.shade = shade
        self.type = type
        self.speed = 0
        self.p = "bike"
        self.name = "Garth"
        self.wheel = 0

    def set_speed(self):
       self.speed = 0
       return True

    def set_wheel_amount(self):
        self.wheel = Wheel()
        self.wheel = Wheel.amount(self.p, self.p)
        print("set_wheel_amount is set to: ", self.wheel)
        return True

    def owner(self):
        print(self.name + " is the owner of the " + self.p)
        return self.name

    def get_wheel_amount(self):
        print("get_wheel_amount is set to: ", self.wheel)
        return self.wheel

    def get_speed(self):
        if self.type in ['BMX', 'bmx', 'Bmx']:
            self.speed = 25
        elif self.type in ['mountain', 'Mountain']:
            self.speed = 8
        elif self.type in ['street', 'Street', 'STREET']:
            self.speed = 15
        return self.speed

    def info(self):
        self.pedal()
        self.owner()
        self.get_speed()
        self.get_engine()
        self.get_wheel_amount()
        print("The average speed of Garth's " + self.type + " bike is " + str(self.get_speed()) + " mph")
        self.color()
        return True

    def color(self):
        print("The color of the bike is: " + self.shade)

    def get_engine(self):
        engineAmount = Engine.does_vehicle_have_engine(self.p)
        if engineAmount > 0:
            print("Since this is a " + self.p + ", it contains an engine")
        else:
            print("Since this is a " + self.p + ", it does not contain an engine")

    def pedal(self):
        if self.type in ['BMX', 'bmx', 'Bmx']:
            print("Since this is not a mountain or street bike, there is no need to pedal")
            return True
        else:
            print("Since this is a mountain or street bike, Garth must pedal the bike")
            return False