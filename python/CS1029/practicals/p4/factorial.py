# Author: Zsolt Kébel
# Date: 30/10/2020

# exercise 9

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))
