# Author: Zsolt Kébel
# Date: 10/02/2021

# *args
#   varying number of positional arguments

# **kwargs
#   varying number of keyword (or named) arguments
#   named argument: ma = 'Audi'

def my_sum(a, b):
    return a + b


def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result


def my_func(**kwargs):
    for i in kwargs.items():
        print(i)


print(my_sum(1, 2, 3, 4, 5, 6))
print(my_func(a=1, b=2, c=3, d=4, e=5, f=6))
