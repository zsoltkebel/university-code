# Author: Zsolt Kébel
# Date: 11/11/2020

total = 0

for i in range(8 * 8):
    total += 2 ** i

rice_grains = [2*i for i in range(0, 64)]

print(total)