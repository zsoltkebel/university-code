# Author: Zsolt Kébel
# Date: 26/01/2021

# A string is a palindrome if it is identical forward and backward.
# For example, “anna”, “civic”, “level” and “hannah” are all examples of palindromic words.
# The program reads a string from the user and determines whether or not it is a palindrome.

word = input("word: ")

palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-i-1]:
        palindrome = False
        break

print("Palindrome: ", palindrome)