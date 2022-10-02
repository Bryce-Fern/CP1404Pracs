OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, 'w')

username = str(input("What is your name?: "))
print(username, file=out_file)
out_file.close()

name = open("name.txt", 'r')
username = name.read()
name.close()
print("Your name is", username)

numbers_file = open("numbers.txt", 'r')
number1 = int(numbers_file.readline())
number2 = int(numbers_file.readline())
numbers_file.close()
print(number1 + number2)

# Is there a way to use one readlines variable instead of using two readline variables to get both numbers and
# then sum the two numbers and print that sum variable? Apologies if this makes no sense when reading, I will ask
# in the next practical for more clarity on when to use readlines over readline.

numbers_file = open("numbers.txt", 'r')
total = 0
for numbers in numbers_file:
    number = int(numbers)
    total += number
numbers_file.close()
print(total)
