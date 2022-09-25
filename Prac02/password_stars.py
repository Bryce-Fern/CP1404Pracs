MIN_Length = 4
print("Please enter a password of at least", MIN_Length, "Characters")
get_password = str(input("Enter Password: "))
num_characters = len(get_password)

while num_characters < MIN_Length:
    print("Password doesn't meet minimum length")
    print("Please enter a password of at least", MIN_Length, "Characters")
    get_password = str(input("Enter Password: "))
    num_characters = len(get_password)
else:
    for i in range(num_characters):
        print('*', end=' ')
    print()

