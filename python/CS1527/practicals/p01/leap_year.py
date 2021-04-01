# Author: Zsolt Kébel
# Date: 26/01/2021

# The rules for determining whether or not a year is a leap year are as follows:
# • Any year that is divisible by 400 is a leap year;
# • Of the remaining years, any year that is divisible by 100 is not a leap year;
# • Of the remaining years, any year that is divisible by 4 is a leap year;
# • All other years are not leap years.
# The program reads a year from the user and displays a message indicating whether or not it is a leap year.

year = int(input("Year: "))

leapYear = False

if year % 400 == 0:
    # leap year
    leapYear = True
elif year % 100 == 0:
    leapYear = False
elif year % 4 == 0:
    leapYear = True
else:
    leapYear = False

print("Leap year:", leapYear)
