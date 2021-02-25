# Author: Zsolt Kébel
# Date: 21/10/2020

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
n = int(input("n: "))

if a ** n + b ** n == c ** n:
    print("Holy smokes, Fermat was wrong!")
else:
    print("No, that doesn’t work")