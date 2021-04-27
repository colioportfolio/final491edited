import unittest
from parts import Wheel
from parts import Engine
from fordPinto import Car
from bike import Bike


class Test_Parts(unittest.TestCase):

    #function coverage
    def test_amount(self):
        test = Wheel()
        car = "car"
        if self.assertEqual(test.amount(car), 4):
            return

    #edge coverage
    def test_edge_amount(self):
        test = Wheel()
        bus = "bus"
        if self.assertEqual(test.amount(bus), 0):
            return

    def test_does_vehicle_have_engine(self):
        test = Engine()
        car = "car"
        if self.assertEqual(test.does_vehicle_have_engine(car), 1):
            return

class Test_fordPinto(unittest.TestCase):

    def test_get_wheel_amount(self):
        test = Car("red")
        if self.assertEqual(test.get_wheel_amount(), 4):
            return


    def test_owner(self):
        test = Car("red")
        if self.assertEqual(test.owner(), "Wayne"):
            return

    def test_get_speed(self):
        test = Car("red")
        if self.assertIsNotNone(test.get_speed()):
            return

    def test_set_speed(self):
        test = Car("red")
        if self.assertTrue(test.set_speed()):
            return

    def test_get_engine(self):
        test = Car("red")
        if self.assertEqual(test.get_engine(), 1):
            return

    #statement coverage
    def test_info(self):
        test = Car("red")
        if self.assertIsNotNone(test.info()):
            return

class Test_bike(unittest.TestCase):

    def test_set_speed(self):
        test = Bike("RED", "BMX")
        if self.assertTrue(test.set_speed()):
            return

    def test_set_wheel_amount(self):
        test = Bike("RED", "BMX")
        if self.assertTrue(test.set_wheel_amount()):
            return

    def test_owner(self):
        test = Bike("RED", "BMX")
        if self.assertEqual(test.owner(), "Garth"):
            return

    #conditional coverage
    def test_get_wheel_amount(self):
        test = Bike("RED", "BMX")
        if self.assertIsNotNone(test.get_wheel_amount()):
            return

    #branch coverage
    def test_get_speed(self):
        test = Bike("RED", "BMX")
        testTwo = Bike("RED", "mountain")
        testThree = Bike("RED", "street")
        if self.assertEqual(test.get_speed(), 25):
            if self.assertEqual(testTwo.get_speed(), 8):
                if self.assertEqual(testThree.get_speed(), 15):
                    return

    def test_pedal(self):
        test = Bike("RED", "BMX")
        if self.assertTrue(test.pedal()):
            return

class Integration_Testing(unittest.TestCase):

    def test_set_and_get_speed(self):
        test = Car("red")
        if Test_fordPinto.test_set_speed(self):
            if Test_fordPinto.test_get_speed(self):
                if self.assertEqual(test.get_speed(), 110):
                    return

    def test_set_and_get_wheel(self):
        test = Bike("red", "BMX")
        if Test_bike.test_set_wheel_amount(self):
            if Test_bike.test_get_wheel_amount(self):
                if self.assertEqual(test.get_wheel_amount(), 2):
                    return