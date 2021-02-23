# Author: Zsolt Kébel
# Date: 04/02/2021

def to_fahrenheit(celsius):
    return celsius * 9/5 + 32


print("Celsius   Fahrenheit")
for i in range(0, 101, 10):
    print(f"{i},   {to_fahrenheit(i)}")
