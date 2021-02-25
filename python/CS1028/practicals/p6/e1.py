# Author: Zsolt Kébel
# Date: 11/11/2020

def without_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""

    for letter in text:
        if letter.lower() in vowels:
            result += " "
        else:
            result += letter

    return result


print(without_vowels("This is a sample text."))
