# Author: Zsolt Kébel
# Date: 18/11/2020

try:
    info = open("q2.txt", "r")

    lines = info.readlines()

    for line in lines[-10:]:
        print(line.strip("\n"))

    info.close()

except IOError:
    print("Oops an error happened whilst accessing the file..")
