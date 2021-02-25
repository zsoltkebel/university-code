# Author: Zsolt Kébel
# Date: 18/11/2020

numLines = 10

try:
    info = open("q1.txt", "r")

    line = info.readline()
    count = 0
    while count < numLines and line != "":
        line = line.strip()
        print(line)
        count += 1

        line = info.readline()

    info.close()

except IOError:
    print("Oops an error happened whilst accessing the file..")
