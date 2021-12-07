#prime numbers

numberOfPrimes = 50
numberOfPrimesPerLine = 10
count = 0
number = 2

print("the first 50 numbers are")

while count < numberOfPrimes:
    isPrime = True
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1
    if isPrime:
        count += 1
        print(format(number, "5d"), end="")
        if count % numberOfPrimesPerLine == 0:
            print()

    number += 1
