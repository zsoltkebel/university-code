# Author: Zsolt Kébel
# Date: 20/11/2020

A = [6, 7, 8, 9, 10]
B = [1, 2, 3, 4, 5]

U = [[x, y] for x in A for y in B if x % y == 0 ]

print(U)
