# Author: Zsolt Kébel
# Date: 21/10/2020

def median(num1, num2, num3):
    if (num1 < num2 and num1 > num3) or (num1 > num2 and num1 < num3):
        return num1
    elif (num2 < num1 and num2 > num3) or (num2 > num1 and num2 < num3):
        return num2
    else:
        return num3

print(median(12, 11, 10))