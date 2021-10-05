# Author: Zsolt Kébel
# Date: 09/10/2020

from fractions import Fraction

a = Fraction(3, 10)
b = Fraction(4, 15)
print(a, "+", b, "=", a + b)

c = Fraction(1, 4)
d = Fraction(1, 5)
print(c, "+", d, "=", c + d)

e = Fraction(2, 3)
f = Fraction(3, 2)
print(e, "(", 6, "-", f, ")", "=", e * (6  - f))

g = Fraction(1, 2)
h = Fraction(1, 3)
print(f"({g} - {h}) * ({g} - {h}) = {(g - h) * (g - h)}")
