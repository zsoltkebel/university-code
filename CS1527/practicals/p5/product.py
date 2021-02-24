# Author: Zsolt Kébel
# Date: 23/02/2021

# A program that calculates the product of m and n using recursion and addition only

def product(m, n, total=0):
    if m > 0 and n > 0:
        m, n, total = product(m - 1, n, total + n)
    return m, n, total


print(product(4, 3)[2])
