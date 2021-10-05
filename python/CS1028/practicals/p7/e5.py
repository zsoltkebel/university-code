# Author: Zsolt Kébel
# Date: 18/11/2020

import random

wordsFile = open("words.txt", "r")

words = wordsFile.readlines()

numWords = len(words)

# generating two random NUMBERS for getting two different words
firstWordIndex = random.randint(0, numWords - 1)
secondWordIndex = firstWordIndex

while firstWordIndex == secondWordIndex:
    secondWordIndex = random.randint(0, numWords - 1)

# making the first letter in both words uppercase
firstWord = (words[firstWordIndex][0].upper() + words[firstWordIndex][1:]).strip("\n")
secondWord = (words[secondWordIndex][0].upper() + words[secondWordIndex][1:]).strip("\n")

password = firstWord + secondWord

print(password)

wordsFile.close()
