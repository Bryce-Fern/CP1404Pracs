def main():
    numbers = []
    i = 0
    while i in range(5):
        try:
            number = int(input("Number: "))
            numbers.append(number)
            i += 1
        except ValueError:
            print("Invalid input")

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = str(input("What if your username?: "))

if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")

main()
