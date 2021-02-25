# Author: Zsolt Kébel
# Date: 14/10/2020

length1 = float(input("Length of first room: "))
width1 = float(input("Width of first room: "))

length2 = float(input("Length of second room: "))
width2 = float(input("Width of second room: "))

area1 = length1 * width1
area2 = length2 * width2

if area1 == area2:
    print("They are the same")
else:
    print("They are not the same")