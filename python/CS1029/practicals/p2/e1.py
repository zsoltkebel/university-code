# Author: Zsolt Kébel
# Date: 16/10/2020

import collections

# construct a namedtuple, so we can access data like customer.name, customer.age
# see https://docs.python.org/3/library/collections.html#collections.namedtuple
Customer = collections.namedtuple('Customer', 'name, age, money')

# create John and James as a Customer
john = Customer('John', 17, 20)
james = Customer('James', 18, 16)

wine_price = 20


def sell_wine(customer, item_price):
    # only sell wine to customer who is not under 18 and has enough money.
    # Please construct the if conditions
    if customer.age >= 18:
        if customer.money >= item_price:
            print(f'sell red wine to {customer.name}')
        else:
            print(f'Sorry, {customer.name}, you are above 18 but don\'t have enough money.')
    else:
        print(
            f'Sorry, {customer.name}, you are not qualified to purchase this item, because you are under 18.')


# uncomment the following the lines to test your result.
sell_wine(john, wine_price)
sell_wine(james, wine_price)
