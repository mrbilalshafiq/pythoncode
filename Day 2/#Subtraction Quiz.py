#Subtraction Quiz

import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number1 < number2:
    number1, number2 = number2, number1

answer = eval(input(f"What is {number1} - {number2}? "))

if number1 - number2 == answer:
    print("Well Done!")
else:
    print(f"You're wrong, {number1} - {number2} = {number1 - number2}")