#Calculate area of a triangle
side1 = eval(input("Enter length of sides: "))
side2 = eval(input("Enter length of sides: "))
side3 = eval(input("Enter length of sides: "))

s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

print("The area of the triangle is", area)
