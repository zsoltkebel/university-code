# Author: Zsolt Kébel
# Date: 10/02/2021

# DYNAMIC TYPING
# - Python supports 'dynamic typing' - allows us to declare variables
#   without needing to specify their types (int, float, string ...)
# - Later in our code we can assign other data types to the same variable

my_var = 100
print(type(my_var))

my_var = 'Dynamic typing here'
print(type(my_var))

my_var = [1, 2, 3]
print(type(my_var))


# DUCK TYPING
# - Form of polymorphism implemented by Python
# - Duck typing allows us to use any object that provides the required behaviour
#   without forcing it to be a subclass


# Useful Built-Ins
# isinstance(<object>, <classinfo>)
# issubclass(<class>, <classinfo>)
print(isinstance(2, int))
print(issubclass(int, object))
