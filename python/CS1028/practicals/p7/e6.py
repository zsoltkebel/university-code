# Author: Zsolt Kébel
# Date: 18/11/2020

file = open("text.txt")
swFile = open("sensitive_words.txt")

text = file.read()
sensitiveWords = swFile.readlines()
newText = ""

for sensitiveWord in sensitiveWords:
    newText = text.replace(sensitiveWord, "*")

print(newText)

file.close()
swFile.close()
