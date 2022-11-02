from Prac06.guitar import Guitar

"""
Estimated time: 5m
Actual time: 9m
"""


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")


main()

