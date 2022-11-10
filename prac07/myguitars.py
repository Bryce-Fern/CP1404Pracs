class Guitars:

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        return self.year < other.year

    def __str__(self):
        return f"{self.name} first introduced in the year: {self.year}, Cost: ${self.cost}"


def run_test():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitars(parts[0], int(parts[1]), (parts[2]))
        guitars.append(guitar)
        guitars.sort()
    in_file.close()

    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    run_test()
