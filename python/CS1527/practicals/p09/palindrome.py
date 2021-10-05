# Author: Zsolt Kébel
# Date: 25/03/2021

def palindrome(s: str):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def isPalindrome(s):
    return s == s[::-1]

def is_palindrome_permutation(phrase):
    """checks if a string is a permutation of a palindrome"""
    table = [0 for _ in range(ord("z") - ord("a") + 1)]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1

    return countodd <= 1


def char_number(c):
    a = ord("a")
    z = ord("z")
    upper_a = ord("A")
    upper_z = ord("Z")
    val = ord(c)

    if a <= val <= z:
        return val - a

    if upper_a <= val <= upper_z:
        return val - upper_a
    return -1


print(palindrome("ahaa"))
print(palindrome("aha"))
print(isPalindrome("aha"))
