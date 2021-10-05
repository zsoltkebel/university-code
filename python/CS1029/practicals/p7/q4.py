# Author: Zsolt Kébel
# Date: 20/11/2020

def is_reflexive(A, R):
    for x in A:
        if (x, x) not in R:
            return False
    return True


def is_symmetric(R):
    for x_y in R:
        x = x_y[0]
        y = x_y[1]

        if (y, x) not in R:
            return False
    return True


def pairs_with_x(R, x):
    pairs = []
    for x_y in R:
        if x_y[0] == x:
            pairs.append(x_y)
    return pairs


def is_transitive(R):
    for x_y in R:
        x = x_y[0]
        y = x_y[1]
        pairs = pairs_with_x(R, y)

        for y_z in pairs:
            z = y_z[1]
            if (x, z) not in R:
                return False
    return True


# test

A = [6, 7, 1, 2, 10]
B = [1, 2, 3, 4, 5]

product = [(a, b) for a in A for b in B if a % b == 0]

print(product)
print("Reflexive:", is_reflexive(A, product))
print("Symmetric:", is_symmetric(product))
print("Transitive:", is_transitive(product))

x = lambda i, j : [[str(i) + str(j)] for i in A for j in B]
