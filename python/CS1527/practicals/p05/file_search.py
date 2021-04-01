# Author: Zsolt Kébel
# Date: 24/02/2021

import os


def search(path, filename):
    paths = []
    try:
        entries = os.listdir(path)
    except IOError as e:
        print(e)
        print('Its okay :)')
    else:
        for entry in entries:
            # absolute path to entry
            entry_path = os.path.join(path, entry)

            if os.path.isfile(entry_path) and entry == filename:
                paths.append(entry_path)
            elif os.path.isdir(entry_path):
                sub_paths = search(entry_path, filename)
                for sub_path in sub_paths:
                    paths.append(sub_path)
    finally:
        return paths


my_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
absoult_path = '//'  # NOTE THAT THIS IS DIFFERENT ON EVERY COMPUTER
print(search(absoult_path, 'array_stack.py'))
