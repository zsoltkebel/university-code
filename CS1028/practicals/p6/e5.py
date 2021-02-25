# Author: Zsolt Kébel
# Date: 11/11/2020

import math


def numbers(t):
    for s in t:
        print("number:", s, "square:", s ** 2, "square root:", math.sqrt(s))


numbers([18, 25, 3, 88, 60, 22, 89, 99, 20, 150])
