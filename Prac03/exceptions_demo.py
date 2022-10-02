"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur? ValueError occurs when either numerator or denominator receives an input that can't be
# interpreted as an integer

# When will a ZeroDivisionError occur? This occurs when '0' is entered as the number for 'denominator'

# Could you change the code to avoid the possibility of a ZeroDivisionError? Add a while loop for denominator to only
# continue once a value other than 0 is entered
