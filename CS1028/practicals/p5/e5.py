# Author: Zsolt Kébel
# Date: 04/11/2020

average = 0
total = 0

for i in range(1, 8):
    temp = float(input("Temperature: "))
    total += temp

average = total / 7

print("Average temperature:", average)
