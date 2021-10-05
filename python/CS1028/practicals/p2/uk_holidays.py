# Author: Zsolt Kébel
# Date: 14/10/2020

# Prints out the holiday for input date and month.

holidays = [[1, "January", "New Year's Day"],
            [10, "April", "Good Friday"],
            [13, "April", "Easter Monday"],
            [8, "May", "Early May Bank Holiday"],
            [25, "May", "Spring Bank Holiday"],
            [25, "December", "Christmas Day"],
            [28, "December", "Boxing Day"]]

date = int(input("Date: "))
month = input("Month: ")

for holiday in holidays:
    if date == holiday[0] and (month.lower() == holiday[1].lower() or month.lower() == holiday[1][:3].lower()):
        print(holiday[2])
