# Author: Zsolt Kébel
# Date: 21/10/2020

def gcd(x, y):
    r = x % y

    if r == 0:
        return y
    else:
        return gcd(y, r)

print(gcd(30, 20))