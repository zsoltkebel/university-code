# Author: Zsolt Kébel
# Date: 07/10/2020

# Create a program that reads a duration from the user
# as a number of days, hours, minutes, and seconds.
# Compute and display the total number of seconds represented by this duration.

days = int(input("Day(s): "))
hours = int(input("Hour(s): "))
minutes = int(input("Minute(s): "))
seconds = int(input("Second(s): "))

inSeconds = seconds + minutes * 60 + hours * 60 * 60 + days * 60 * 60 * 24

print("Overall seconds:", inSeconds)
