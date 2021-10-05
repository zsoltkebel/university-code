# Author: Zsolt Kébel
# Date: 09/10/2020

from fractions import Fraction

print(f"|100| = {abs(100)}")

a = Fraction(-6, 24)
print(f"|{a}| = {abs(a)}")

print(f"-1 - |1 - |-1|| = {-1 - abs(1 - abs(-1))}")

print(f"(-2) * 6 = {-2 * 6}")

print(f"||-6| - |-4|| = {abs(abs(-6) - abs(-4))}")  # e

b = Fraction(7 - 12, 12 -7)
print(f"|{b}| = {abs(b)}")  # f
