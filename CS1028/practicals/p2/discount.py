# Author: Zsolt Kébel
# Date: 14/10/2020

# Discount is offered on the total amount on the receipt as follow:
# • 0 discounts for less than 10 items
# • 20% discount between 10 and 19 items
# • 30% discount between 20 and 30 items
# • 50% for more than 30 items.

amount = float(input("Amount: "))
numOfItems = int(input("NUmber of items: "))

finalAmount = 0

if numOfItems < 10:
    finalAmount = amount
elif numOfItems < 20:
    finalAmount = amount * 0.8
elif numOfItems <= 30:
    finalAmount = amount * 0.7
else:
    finalAmount = amount * 0.5

print(f"total amount: {finalAmount}")