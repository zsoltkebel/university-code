# Author: Zsolt Kébel
# Date: 11/11/2020

def only_even(t):
    result = []
    for s in t:
        if s % 2 == 0:
            result.append(s)
    return result


print(only_even([1, 3, 5, 2, 1]))
