# Author: Zsolt Kébel
# Date: 20/11/2020

# Produces the cartesian product of one set

A = [1, 2, 3, 4, 5]

product = [[a, b] for a in A for b in A]

print(product)
