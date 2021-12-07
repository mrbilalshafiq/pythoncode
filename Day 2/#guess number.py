#guess number

import random
number = random.randint(0, 101)
print("Magic Number Game")

guess = -1
while guess != number:
    guess = eval(input("Enter your guess: "))
    if guess == number:
        print("Yes, the number is", number)
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")