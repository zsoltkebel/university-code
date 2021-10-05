# Author: Zsolt Kébel
# Date: 11/10/2020

from decimal import Decimal

temp = Decimal(input("Please enter the temperature (Celsius): "))
wind = Decimal(input("Please enter the wind speed (km/h): "))

# do the calculation with the given formula
windChillIndex = Decimal("13.12") + Decimal("0.6215") * temp\
                 - Decimal("11.37") * wind ** Decimal("0.16")\
                 + Decimal("0.3965") * temp * wind ** Decimal("0.16")

print("Wind Chill Index:", windChillIndex)
