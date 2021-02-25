# Author: Zsolt Kébel
# Date: 21/10/2020

day = int(input("Day: "))
month = int(input("Month: "))

def isMagicDate(day, month, year):
    return day * month == year

