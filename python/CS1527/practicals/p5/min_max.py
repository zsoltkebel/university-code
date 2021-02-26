# Author: Zsolt Kébel
# Date: 23/02/2021

# Program that finds the minimum and maximum value in a sequence without using a loop

import unittest
from collections import namedtuple


def find_min_max(arr):
    extreme_values = namedtuple('value', ['min', 'max'])

    if len(arr) > 1:
        extremes_of_subarray = find_min_max(arr[1:])
        return extreme_values(min(arr[0], extremes_of_subarray.min), max(arr[0], extremes_of_subarray.max))
    else:  # base case
        try:
            return extreme_values(arr[0], arr[0])
        except IndexError:
            return extreme_values(None, None)


class Tests(unittest.TestCase):

    def test1(self):
        s = [2, 1, 4, 5, 10, 0, 3, -3]
        self.assertEqual(find_min_max(s), (-3, 10))

    def test2(self):
        s = [2, 4, 0, -3]
        self.assertEqual(find_min_max(s), (-3, 4))

    def test3(self):
        s = []
        self.assertEqual(find_min_max(s), (None, None))


if __name__ == '__main__':
    unittest.main()

