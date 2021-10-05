# Author: Zsolt Kébel
# Date: 11/11/2020

def times_table(number):
    result = []
    for i in range(1, 13):
        result.append(number * i)
    return result


print(times_table(4))
