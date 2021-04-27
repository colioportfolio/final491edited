import unittest
from parts import Wheel
from parts import Engine
from fordPinto import Car
from bike import Bike


class Test_Parts(unittest.TestCase):

    #function coverage
    def test_amount(self):
        print("Function coverage.  ")
        test = Wheel()
        car = "car"
        if self.assertEqual(test.amount(car), 4):
            return

    #edge coverage
    def test_edge_amount(self):
        print("Edge coverage. ")
        test = Wheel()
        bus = "bus"
        if self.assertEqual(test.amount(bus), 0):
            return

    def test_does_vehicle_have_engine(self):
        print("have_engine test. ")
        test = Engine()
        car = "car"
        if self.assertEqual(test.does_vehicle_have_engine(car), 1):
            return

class Test_fordPinto(unittest.TestCase):

    def test_get_wheel_amount(self):
        print("car get_wheel_amount test. ")
        test = Car("red")
        if self.assertEqual(test.get_wheel_amount(), 4):
            return


    def test_owner(self):
        print("car test_owner test. ")
        test = Car("red")
        if self.assertEqual(test.owner(), "Wayne"):
            return

    def test_get_speed(self):
        print("car get_speed test. ")
        test = Car("red")
        if self.assertIsNotNone(test.get_speed()):
            return

    def test_set_speed(self):
        print("car set_speed test. ")
        test = Car("red")
        if self.assertTrue(test.set_speed()):
            return

    def test_get_engine(self):
        print("car get_engine test. ")
        test = Car("red")
        if self.assertEqual(test.get_engine(), 1):
            return

    #statement coverage
    def test_info(self):
        print("car test_info test. ")
        test = Car("red")
        if self.assertIsNotNone(test.info()):
            return

class Test_bike(unittest.TestCase):

    def test_set_speed(self):
        print("bike set_speed test. ")
        test = Bike("RED", "BMX")
        if self.assertTrue(test.set_speed()):
            print("value set")
            return

    def test_set_wheel_amount(self):
        print("bike set_wheel test. ")
        test = Bike("RED", "BMX")
        if self.assertTrue(test.set_wheel_amount()):
            return

    def test_owner(self):
        print("bike test_owner test. ")
        test = Bike("RED", "BMX")
        if self.assertEqual(test.owner(), "Garth"):
            return

    #conditional coverage
    def test_get_wheel_amount(self):
        print("bike get_wheel_amount test. ")
        test = Bike("RED", "BMX")
        if self.assertIsNotNone(test.get_wheel_amount()):
            return

    #branch coverage
    def test_get_speed(self):
        print("bike get_speed test. ")
        test = Bike("RED", "BMX")
        testTwo = Bike("RED", "mountain")
        testThree = Bike("RED", "street")
        if self.assertEqual(test.get_speed(), 25):
            if self.assertEqual(testTwo.get_speed(), 8):
                if self.assertEqual(testThree.get_speed(), 15):
                    return

    def test_pedal(self):
        print("bike test_pedal test. ")
        test = Bike("RED", "BMX")
        if self.assertTrue(test.pedal()):
            return

class Integration_Testing(unittest.TestCase):

    def test_set_and_get_speed(self):
        print("car set/get speed integration test. ")
        test = Car("red")
        if Test_fordPinto.test_set_speed(self):
            if Test_fordPinto.test_get_speed(self):
                if self.assertEqual(test.get_speed(), 110):
                    return

    def test_set_and_get_wheel(self):
        print("bike set/get wheel integration test. ")
        test = Bike("red", "BMX")
        if Test_bike.test_set_wheel_amount(self):
            if Test_bike.test_get_wheel_amount(self):
                if self.assertEqual(test.get_wheel_amount(), 2):
                    return