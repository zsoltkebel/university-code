# Author: Zsolt Kébel
# Date: 02/12/2020

# Asks the user for an element, and checks whether the element exists in the
# list using binary search.

import random


def make_list_random(n):
    return [random.randint(0, 100) for i in range(n)]


def make_list_input(n):
    l = []
    for i in range(n):
        l.append(int(input(f"element {i}: ")))

    return l


def sort(l):
    for i in range(0, len(l)):
        for j in range(i + 1, len(l)):
            pass


def binary_search(e, t):
    l = 0
    r = len(t) - 1

    while l <= r:
        m = (l + r) // 2

        if t[m] < e:
            l = m + 1
        elif t[m] > e:
            r = m - 1
        else:
            return m

    return -1


listSize = int(input("list size:"))
print(make_list_random(listSize))

l = make_list_input(listSize)
print(l)

print(binary_search(2, l))