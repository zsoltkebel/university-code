# Author: Zsolt Kébel
# Date: 04/03/2021
import sys

import sys

first_n = 10

try:
    with open(sys.argv[1], 'r') as f:
        for i in range(first_n):
            line = f.readline().strip()  # remove newline character
            print(line)
except IOError:
    print('Something is not good')
