from abc import ABCMeta, abstractmethod

class Wheel:
    x = ''
    count = 0

    def __init__(self):
        self.wheelAmount = 0

    def amount(self, x):
        if x in ["car"]:
            print("This is a:", x)
            count = 4
            return count
        if x in ["bike"]:
            print("This is a:", x)
            count = 2
            return count
        else:
            print("This is a", x, "so it does not apply")
            count = 0
            return count
        return count

class Vehicle(ABCMeta):

    @abstractmethod
    def __init__(self, vehicle, name):
        self.vehicle = vehicle
        self.owner = name

    @abstractmethod
    def owner(self):
        pass
    @abstractmethod
    def get_speed(self, vehicle):
        pass
    @abstractmethod
    def color(self):
        pass
    @abstractmethod
    def get_engine(self):
        pass

class Engine:

    def __init__(self):
        self.engine = 0

    def does_vehicle_have_engine(self, x):
        if x in ["car"]:
            return 1
        else:
            return 0