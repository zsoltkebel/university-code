# Author: Zsolt Kébel
# Date: 23/02/2021

# Program that finds the minimum and maximum value in a sequence without using a loop

def find_min_max(s):
    if len(s) > 1:
        min_val, max_val = find_min_max(s[1:])
        return min(s[0], min_val), max(s[0], max_val)
    elif len(s) == 1:
        return s[0], s[0]  # base case
    else:
        return None, None


s = [2, 1, 4, 5, 10, 0, 3, -3]

minimum,  maximum = find_min_max(s)

print('min:', minimum)
print('max:', maximum)
