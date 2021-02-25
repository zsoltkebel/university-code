# Author: Zsolt Kébel
# Date: 11/11/2020

def sum_of_digits(text):
    total = 0

    for digit in text:
        total += int(digit)

    return total


print(sum_of_digits("3454"))
