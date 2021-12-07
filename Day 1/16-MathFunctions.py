x = x1 = 10
x2 = n = 2
x3 = 20
###Simple Built In Python Functions###
print(abs(x)) #Returns the absolute value for x
print(max(x1, x2, x3)) #Returns the largest among x1, x2 & x3
print(min(x1, x2, x3)) #Returns the smallest among x1, x2 & x3
print(pow(x, x2)) #Same as x ** x2
print(round(x)) #Returns an integer nearest to x. If x is equally close to two integers, the even one is returned.
print(round(x, n)) #Returns the float value rounded to n digits after the decimal point.

print("\n")

###Mathematical Functions###
import math #import math module to use the math functions

print(math.fabs(x)) #Returns the absolute value for x as a float
print(math.ceil(x)) #Rounds x up to its nearest integer and returns that integer 
print(math.floor(x)) #Rounds x down to its nearest integer and returns that integer
print(math.exp(x)) #Returns the exponential function of x (e ** x)
print(math.log(x)) #Returns the natural logarithm of x
print(math.sqrt(x)) #Returns the square root of x
print(math.sin(x)) #Returns the sine of x. X represents an angle in radians
print(math.tan(x)) #Returns the tangent of x. x represents an angle in radians. 
print(math.degrees(x)) #Converts angle from x from radians to degrees
print(math.radians(x)) #Converts angle x from degrees to radians

print("\n")
#Test algebraic functions
print("sqrt(4.0) =", math.sqrt(4.0))