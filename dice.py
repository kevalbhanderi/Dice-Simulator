import random

while True:
    print("1. Roll The Dice \n2.Exit")
    user = int(input("Enter Your Choice : "))
    if user == 1:
        number = random.randint(1,6)
        print(number)
    else:
        break
