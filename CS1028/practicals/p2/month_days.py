# Author: Zsolt Kébel
# Date: 14/10/2020

month = input("month name: ")

if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("31 days")
elif month == "February":
    print("28 or 29 days")
else:
    print("30 days")