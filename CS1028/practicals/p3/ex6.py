# Author: Zsolt Kébel
# Date: 21/10/2020

def is_triangle(a, b, c):
    return not(a > b + c or b > a + c or c > a + b)

print(is_triangle(1, 4, 3))