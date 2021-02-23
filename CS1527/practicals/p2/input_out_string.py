# Author: Zsolt Kébel
# Date: 03/02/2021

class InputOutString:

    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s)


in_out = InputOutString()

in_out.get_string()
in_out.print_string()