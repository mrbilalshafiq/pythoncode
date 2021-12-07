import random
import time

correctCount = 0
count = 0

startTime = time.time()

while count < 5:
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    
    if number1 < number2:
        number1, number2 = number2, number2
    
    answer=eval(input(f"What is {number1} - {number2}? "))

    if number1 - number2 == answer:
        print("You are correct")
        correctCount += 1
    else:
        print(f"Wrong! \n {number1} - {number2} = {number1 - number2}")
        count += 1

endTime = time.time()

testTime = int(endTime-startTime)

print(f"Correct count is {correctCount}, out of 5 questions in {testTime} seconds.")