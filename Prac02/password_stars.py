MIN_Length = 4


def get_password():
    global password, num_characters
    print("Please enter a password of at least", MIN_Length, "Characters")
    password = str(input("Enter Password: "))
    num_characters = len(password)


get_password()

while num_characters < MIN_Length:
    print("Password doesn't meet minimum length")
    get_password()
else:
    for i in range(num_characters):
        print('*', end=' ')
    print()
