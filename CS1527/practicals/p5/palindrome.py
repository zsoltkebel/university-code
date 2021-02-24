# Author: Zsolt Kébel
# Date: 24/02/2021

def is_palindrome(s):
    if len(s) > 1:
        return s[0] == s[len(s) - 1] and is_palindrome(s[1:-1])
    else:
        return True


print(is_palindrome('racecar'))
