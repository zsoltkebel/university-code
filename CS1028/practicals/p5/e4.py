# Author: Zsolt Kébel
# Date: 04/11/2020

number = float(input("Number: "))
highest = number

while number != 0:
    if number > highest:
        highest = number

    number = float(input("Number: "))

print("Highest:", highest)