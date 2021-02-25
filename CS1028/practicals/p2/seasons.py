# Author: Zsolt Kébel
# Date: 14/10/2020

# The first day of seasons of the year are as follow:
# Spring: March 20
# Summer: June 21
# Fall: September 22
# Winter: December 21
# Display the season associated with the date.

month = "Mar"
date = 23

if month == "Jan" or month == "Feb":
    print("Winter")

elif month == "Mar":
    if date < 20:
        print("Winter")
    else:
        print("Spring")

elif month == "Apr" or month == "May":
    print("Spring")

elif month == "Jun":
    if date < 21:
        print("Spring")
    else:
        print("Summer")

elif month == "July" or month == "Aug":
    print("Summer")

elif month == "Sep":
    if date < 22:
        print("Summer")
    else:
        print("Fall")

elif month == "Oct" or month == "Nov":
    print("Fall")

elif month == "Dec":
    if date < 21:
        print("Fall")
    else:
        print("Winter")
