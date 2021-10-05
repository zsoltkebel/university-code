# Author: Zsolt Kébel
# Date: 14/10/2020

numOfSides = int(input("Number of sides: "))

if numOfSides == 3:
    nameOfShape = "Triangle"
elif numOfSides == 4:
    nameOfShape = "Rectangle"
elif numOfSides == 5:
    nameOfShape = "Pentagon"
elif numOfSides == 6:
    nameOfShape = "Hexagon"
elif numOfSides == 7:
    nameOfShape = "Heptagon"
elif numOfSides == 8:
    nameOfShape = "Octagon"
elif numOfSides == 9:
    nameOfShape = "Enneagon"
elif numOfSides == 10:
    nameOfShape = "Decagon"
else:
    nameOfShape = "Name of shape is not defined in the prgoram"

print("Name of shape:", nameOfShape)
