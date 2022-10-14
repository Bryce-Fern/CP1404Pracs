import random

max_number = 45
min_number = 1
numbers_per_line = 6


def main():
    quick_picks = int(input("How many quick picks?: "))
    while quick_picks < 0:
        print("Invalid amount of quick picks")
        quick_picks = int(input("How many quick picks?: "))

    for g in range(quick_picks):
        quick_pick = []
        for h in range(numbers_per_line):
            numbers = random.randint(min_number, max_number)
            quick_pick.append(numbers)
            quick_pick.sort()
        print(' '.join(f"{number:2}" for number in quick_pick))


main()
