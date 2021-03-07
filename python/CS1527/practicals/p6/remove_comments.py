# Author: Zsolt Kébel
# Date: 04/03/2021

# Removes python comments starting with # from a file


try:
    source_name = input('Source file: ')
    with open(source_name, 'r') as file_source:
        target_name = input('Target file: ')
        with open(target_name, 'w') as file_target:
            lines = file_source.readlines()
            for line in lines:
                if line.__contains__(' #'):  # changing line if it contains comment
                    line = line[0:line.find(' #')]
                    line += '\n'
                file_target.write(line)
except IOError:
    print('Something is not good')