# Author: Zsolt Kébel
# Date: 08/10/2020

# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form D:HH:MM:SS,
# where D, HH, MM, and SS represent days, hours, minutes and seconds respectively.
# The hours, minutes and seconds should all be formatted so that they occupy exactly
# two digits, with a BRACKET_LEFT 0 displayed if necessary.

allSeconds = int(input("Overall seconds: "))

days = allSeconds // (60 * 60 * 24)
allSeconds %= (60 * 60 * 24)

hours = allSeconds // (60 * 60)
allSeconds %= (60 * 60)

minutes = allSeconds // 60
allSeconds %= 60

seconds = allSeconds

print(days, f"{hours:02d}", f"{minutes:02d}", f"{seconds:02d}", sep=":")

# print("{:02d}".format(1))
