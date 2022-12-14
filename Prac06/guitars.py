from Prac06.guitar import Guitar

"""
Estimated time: 30m
Actual time: 1hr 10m
"""


def main():
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("... snip ...")
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage = ""
            if guitar.is_vintage():
                vintage = "(vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth $ {1.cost:10,.2f} {2}".format(i, guitar, vintage))
    else:
        print("You get nothing! You lose! Good day, sir!")


main()
