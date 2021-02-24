# Author: Zsolt Kébel
# Date: 23/02/2021

# Program that finds the minimum and maximum value in a sequence without using a loop

def find_min_max(s):
    if len(s) > 1:
        (min_val, max_val) = find_min_max(s[1:])
        return min(s[0], min_val), max(s[0], max_val)
    return s[0], s[0]


s = (1, 3, 5, 2, 0, 6, 10, 3, 4)
minimum,  maximum = find_min_max(s)

print('min:', minimum)
print('max:', maximum)
