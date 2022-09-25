from random import randint


def main():
    score = user_score()
    get_grade(score)


def get_grade(score):
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Passable")
        else:
            print("Bad")


def user_score():
    score = float(input("Enter score: "))
    return score


score = randint(1, 100)

main()
