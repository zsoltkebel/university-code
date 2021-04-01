# Author: Zsolt Kébel
# Date: 26/01/2021

# The Chinese zodiac assigns animals to years in a 12-year cycle.
# 2000 was the year of the dragon, 2011 was the year of the hare.
# The pattern repeats itself, with 2012 being another year of the dragon, and 1999 being another year of the hare.

year = int(input("Year: "))

remainder = year % 12 - 8
zodiacs = ["Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare"]

print("The year of", zodiacs[remainder])
