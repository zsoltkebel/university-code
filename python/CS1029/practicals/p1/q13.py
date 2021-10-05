# Author: Zsolt Kébel
# Date: 09/10/2020

from decimal import Decimal

# a
a1 = Decimal("3.5")
a2 = Decimal("20.78")
a3 = Decimal("4.53")
print(f"a)  ({a1} + {a2}) * {a3} = {(a1 + a2) * a3}")

# b
b1 = Decimal("9.7")
b2 = Decimal("4.5")
b3 = Decimal("5.9")
b4 = Decimal("3.4")
print(f"b)  ({b1} - {b2}) * ({b3} + {b4}) = {(b1 - b2) * (b3 + b4)}")

# c
c1 = Decimal("3.2")
c2 = Decimal("8.8")
c3 = Decimal("9.7")
c4 = Decimal("4.3")
print(f"c)  |{c1} - {c2}| * |{c3} - {c4}| = {abs(c1 - c2) * abs(c3 - c4)}")

# d
d1 = Decimal("87687")
d2 = Decimal("8162876")
d3 = Decimal("5.24")
print(f"d)  |{d1} - {d2}| * {d3} = {abs(d1 - d2) * d3}")
