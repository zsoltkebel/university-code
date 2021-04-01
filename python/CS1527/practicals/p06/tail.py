# Author: Zsolt Kébel
# Date: 04/03/2021

import sys

try:
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        last_lines = lines[-3:]
        for l in last_lines:
            print(l)
except IOError:
    print('Something is not good')
