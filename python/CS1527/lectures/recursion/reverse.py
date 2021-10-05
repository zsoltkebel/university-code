# Author: Zsolt Kébel
# Date: 21/02/2021

def reverse(s, start, end):
    """Reverse elements in implicit slice s[start:end]"""
    if start < end - 1:                                 # if at least 2 elements
        print('reverse:', s)
        s[start], s[end - 1] = s[end - 1], s[start]     # swap first and last
        reverse(s, start + 1, end - 1)                  # recur on rest


def reverse_iterative(s):
    """Reverse elements in sequence s"""
    start, stop = 0, len(s)
    while start < stop - 1:
        print('reverse:', s)
        s[start], s[stop - 1] = s[stop - 1], s[start]
        start, stop = start + 1, stop - 1


if __name__ == '__main__':
    s = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(s)
    reverse(s, 0, len(s))
    print(s)
    reverse_iterative(s)
    print(s)
