# Author: Zsolt Kébel
# Date: 18/11/2020

inputFilename = input("Input Filename: ")
outputFilename = input("Output Filename: ")

inputFile = open(inputFilename, "r")
outputFile = open(outputFilename, "w")

for line in inputFile:
    if len(line.strip()) > 0 and line.strip()[0] == "#":
        # do nothing
        pass
    else:
        outputFile.write(line)

inputFile.close()
outputFile.close()
