## DATA TYPES

# String
name = "Steve"
print(name)

# Boolean
discount = False 
print(False)

# Integer
age = 32 
print(age)

# Float
wallet = 29.95 
print(wallet)

## BUILT IN FUNCTIONS

print("Hello World") # Displays "Hello World"

name = input("Hello, what is your name? ")
age = int(input("and what is your age? "))

print(type("Hello World")) # Displays "<class 'str'>", showing it is a string

## MATHS

Basic mathematics can be performed in Python:

Addition - '+'
Subtraction - '-'
True Division - '/'
Floor Division - '//' (The whole integer result after one number is divided by another)
Multiplication - '*'
Powers - '**'
Modulo - '%' (The remainder after one number is divided by another)
There are many other built-in mathematical functions that can be useful. They are included in a package called math - see more information here.

Python will execute mathematics using BIDMAS:

B - Brackets - (, )
I - Indices - **
D - Division - /, //
M - Multiplication - *
A - Addition - +
S - Subtraction - -
You may also know the acronym as BODMAS or PEDMAS, but they are all equivalent.

Based on this, we can see Python will execute anything inside brackets first, then indices/powers, then division, etc..

Note that Python is left-associative, so if two expressions share the same precedence, it will interpret the left-most expression first.

#Assigning multiple variables with the same value
x = y = z = 1

print(x, y, z)

print(x*y*z)

print(x+y+z)

print(str(x)+str(y)+str(z))

print("x = ", x, ", y = ", y, ", and z = ", z)

## F strings

age = 25
f"John is {age} years old"
'John is 25 years old'

f"John will be {age+10} years old in 10 years!
'John will be 35 years old in 10 years!'

## ESCAPE CHARACTERS
"Hello, they call me \"Jeff\""

Other key escape characters include:

Character	Result
\\	Backslash
\n	New Line
\t	Tab

##INTERGERS and FLOATS
int(3.6)
3

float(3)
3.0

##BOOLEAN
Boolean
A boolean (bool for short) can only store two possible values, True or False.
Note that booleans are a subclass of integers, where True is equivalent to 1, and False is equivalent to 0.

