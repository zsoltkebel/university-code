# Author: Zsolt Kébel
# Date: 14/10/2020

# Decides if input is a vowel (a, e, o, i, u), sometimes vowel sometimes not (y) or consonant otherwise.

letter = input("Letter: ")

if letter == "a" or letter == "e" or letter == "o" or letter == "i" or letter == "u":
    print("Vowel")
elif letter == "y":
    print("sometimes vowel, sometimes consonant")
else:
    print("consonant")
