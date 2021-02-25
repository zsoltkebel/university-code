# Author: Zsolt Kébel
# Date: 04/11/2020

def price(age):
    if age <= 2:
        return 0
    elif age <= 12:
        return 14
    elif age >= 65:
        return 18
    else:
        return 23


user_input = input("Age: ")
total_price = 0

while user_input != "":
    age = int(user_input)
    total_price += price(age)

    user_input = input("Age: ")

print("Total price:", total_price)
