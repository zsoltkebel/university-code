# Author: Zsolt Kébel
# Date: 04/02/2021

class StringException(Exception):

    def __init__(self, msg):
        self.msg = msg