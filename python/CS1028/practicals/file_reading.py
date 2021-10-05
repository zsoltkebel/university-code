# Author: Zsolt Kébel
# Date: 16/12/2020

file = open("text.txt", "r")

for line in file:
    print(line)
    print(".")

for n in range(8, 0, -2):
    print(n)

print(int(43.5697))