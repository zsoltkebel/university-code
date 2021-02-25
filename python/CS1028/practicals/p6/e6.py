# Author: Zsolt Kébel
# Date: 11/11/2020

def print_down(text):
    for i in range(len(text)):
        char = text[i]
        print(char)


def print_up(text):
    i = len(text) - 1
    while i >= 0:
        char = text[i]
        print(char)
        i -= 1


print_up("This text is upside down.")