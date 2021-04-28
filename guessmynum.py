import random

command = ""
number = random.randint(1, 10)
guess = 0
hope = 0

print(number)

print(
    "In this game you will guess my number and you have three guess only.\nWhat is my number: "
)

while guess != 3:
    command = int(input(">> "))
    guess += 1
    print(guess)
    if (command == number):
        print("nice you are a good guesser.")
        break
    elif (guess == 3):
        print("you lose")
    else:
        print("try once again")
