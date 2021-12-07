import random

number1 = random.randint(0,10)
number2 = random.randint(0,10)

if number1 < number2:
    number1, number2 = number2, number1

answer = eval(input(f"What is {number1} - {number2}? "))

while number1 - number2 != answer:
    answer = eval(input(f"Sorry, try again! What is {number1} - {number2}? "))

print("Well done")