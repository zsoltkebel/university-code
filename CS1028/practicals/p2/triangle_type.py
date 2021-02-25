# Author: Zsolt Kébel
# Date: 14/10/2020

# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene.

print("Please enter the length of sides of a triangle.")
a = float(input("side 1: "))
b = float(input("side 2: "))
c = float(input("side 3: "))

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or a == c or b == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
