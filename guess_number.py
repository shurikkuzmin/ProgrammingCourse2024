import random

computer_number = random.randint(1,20)

while True:
    my_number = int(input("Please enter your number: "))
    if computer_number > my_number:
        print("I guessed larger number")
    if computer_number < my_number:
        print("I guessed smaller number")
    if computer_number == my_number:
        print("Bingo!")
        break
print("The End")