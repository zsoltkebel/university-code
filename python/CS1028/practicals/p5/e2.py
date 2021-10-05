# Author: Zsolt Kébel
# Date: 04/11/2020

total = 0

for i in range(365):
    total += i

print(total // 100, "pounds", total % 100, "pence")
