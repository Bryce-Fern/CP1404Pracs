"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from Prac06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    limo = Car(100)
    limo.name = "Limo"
    my_car.name = "Car"
    my_car.drive(30)
    limo.add_fuel(20)
    limo.drive(115)

    # print(f"Car has fuel: {my_car.fuel}")
    print(my_car)
    # print(f"Limo has fuel: {limo.fuel}")
    print(limo)


main()