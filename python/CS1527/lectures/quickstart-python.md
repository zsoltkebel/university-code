# Quickstart Guide for Python
A Quickstart Guide for writing code in Python.

*"Python is an experiment in how much freedom programmers need. Too much freedom and nobody can read another's code;
too little and expressiveness is endangered."*
\- Guido van Rossum

---

#### Table of Contents
- [Variables](#variables)
- [`#comments`](#comments-in-code)
- [Built-in Collections (arrays)](#built-in-collections)
- [`if` Statements](#if-statements)
- [`for` Loops](#for-loops)
- [`while` Loops](#while-loops)
- [Exception Handling `try: ... except:`](#exception-handling)
- [Classes & Objects](#classes--objects)
- [Inheritance](#inheritance)
- [`if __name__ == '__main__':` guard](#if-__name__--__main__-guard)

---

### Variables
No need to explicitly specify type of the variables.
```python
name = 'John'  # string
age = 24       # int
score = 95.0   # float
```

Built-in data types
- Text Type:	`str`
- Numeric Types:	`int`, `float`, `complex`
- Sequence Types:	`list`, `tuple`, `range`
- Mapping Type:	`dict`
- Set Types:	`set`, `frozenset`
- Boolean Type:	`bool`
- Binary Types:	`bytes`, `bytearray`, `memoryview`

Strings in Python are surrounded by either `'`, or `"`, so `'hello'` is the same as `"hello"`.
Pick one style and stick to it.

### Comments in Code
```python
# inline comments

"""Single line docstring"""

"""Multiline docstring
for longer documentation
"""
```
### Built-in Collections
These are sometimes referred to as arrays.

```python
list_numbers = [1, 2, 3, 4, 5]   # declaring a list using brackets
tuple_numbers = (1, 2, 3, 4, 5)  # declaring a tuple using parentheses
set_numbers = {1, 2, 3, 4, 5}    # declaring a set curly brackets
dictionary_car = {               # declaring a dictionary
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

When deciding which collection to use, think about what functionality you need:

| Built-in collection | Ordered | Changeable | Allow duplicate values | Comments
| --- |:-------:|:----------:|:----------------------:| -------------|
List | ✅ | ✅ | ✅ | Items are indexed, the first item has index [0], the second item has index [1] etc.
Tuple | ✅ | ❌ | ✅ | Items are indexed, the first item has index [0], the second item has index [1] etc.
Set | ❌ | ❌ | ❌ | Items can appear in a different order every time you use them, and cannot be referred to by index or key.
Dictionary | ✅ | ✅ | ❌ | Are used to store data values in `key:value` pairs.

### `if` statements
In an `if-elif-else` statement only one branch is going to be executed.
```python
if a == b:
    # only one of these is going to be executed
elif a > b:
    # only one of these is going to be executed
else:
    # only one of these is going to be executed
```

Supported logical conditions:
- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

When comparing a variable to `None` use `is` instead of `==`.
```python
if value is None:
    # do something
```

### `for` loops
```python
for e in [1, 2, 3, 4, 5]:  # iterating over a sequence
    print(e)

for c in 'some string':  # iterate through each character in the string
    print(c)

for i in range(10):  # iterating over NUMBERS from 0 (including) to 10 (excluding)
    print(i)

for i in range(start, stop, step):  # iterating through NUMBERS from [start] to [stop] incrementing by [step] every time
    print(i)
```

### `while` loops
```python
i = 1
while i < 6:  # while loop body gets executed over and over again until the condition holds
    print(i)
    i += 1
```

### Functions
```python
def my_function():
    # do something
```

### Exception Handling
```python
try:
    # try doing something here that might cause the program to break
    1 / 0
except ZeroDivisionError as e:
    # code here is executed only if an exception of type ZeroDivisionError was raised
    print(e)
else:
    # code here is executed only if there were no exceptions raised
    ...
finally:
    # code here gets executed no matter what
    ...
```
`else:` and `finally:` branches are optional.
### Classes & Objects
```python
class Point:
    def __init__(self, x, y):  # this method is always executed when the class is being initiated.
        self.x = x  # assign values to object properties
        self.y = y

    def area(self):  # public method
        return self.width * self.length

    def _area(self):  # protected method (single BRACKET_LEFT underscore)
        ...
    
    def __area(self):  # private method (double BRACKET_LEFT underscores)
        ...


center = Point(3, 6)  # creating an object of Point class
center.x  # accessing properties
center.y = 5  # setting properties
```
### Inheritance

### `if __name__ == '__main__':` guard
```python
if __name__ == '__main__':
    ...  # code here gets executed only if you run this module as the main program
```
More on this on [StackOverflow](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

---

Inspired by:
- [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp)
- [The Best of the Best Practices (BOBP) Guide for Python](https://gist.github.com/sloria/7001839)
- [Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/index.html)