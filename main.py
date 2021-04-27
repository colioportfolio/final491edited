from bike import Bike
from fordPinto import Car
from parts import Vehicle

checker = 0
checker2 = 0
checker3 = 0


def wrong_bike():
    print("Sorry! That currently is not a bike option")


while checker == 0:
    user = input("Hi there! is this Wayne or Garth? ")
    if user in ["Garth", "garth", "GARTH"]:
        bikeType = input("Hello Garth! What kind of bike are you riding? (BMX, mountain, or street?) ")
        while checker2 == 0:
            if bikeType in ["Bmx", "BMX", "bmx", "mountain", "Mountain", "MOUNTAIN", "street", "Street",
                            "STREET"] and checker == 0:
                checker2 = 1
            else:
                bikeType = input(
                    "That is not an option. Please input one of the three choices: BMX, Mountain, or Street ")
        while bikeType in ["Bmx", "BMX", "bmx", "mountain", "Mountain", "MOUNTAIN", "street", "Street",
                           "STREET"] and checker3 == 0:
            color = input("I see. What color is your " + bikeType + " bike? ")
            print("Understood. Here is some info about your bike class: ")

            garthBike = Bike(color, bikeType)
            garthBike.info()
            checker3 = 1
            checker = 1




    elif user in ["Wayne", "wayne", "WAYNE"]:
        # Create Wayne's car
        carColor = input(
            "Hi Wayne! I understand you don't have the finances for many options, so you only have a Ford Pinto. What "
            "color is it? ")
        wayneCar = Car(carColor)
        wayneCar.info()
        checker = 1

    else:
        print("Sorry! This is only for Garth or Wayne.")
