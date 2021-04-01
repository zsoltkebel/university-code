# Author: Zsolt Kébel
# Date: 04/03/2021

# Concatenates files passed as command line parameters

import sys

try:
    filenames = sys.argv[1:]
    print('Concatenating the following files:', filenames)

    with open('output.txt', 'a') as target_file:
        for filename in filenames:
            with open(filename, 'r') as source_file:
                target_file.writelines(source_file.readlines())
                target_file.write('\n')
except IOError:
    print('Something is not good')
