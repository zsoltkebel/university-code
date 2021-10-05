
### Naming
- `CamelCase` for Classes
- `lower_case_with_undescores` for variables, functions, methods, packages, modules
- `_single_leading_underscore(self, ...)` for protected methods
- `__double_leading_underscore(self, ...)` for private methods
- `ALL_CAPS_WITH_UNDERSCORES` for constants

### Code correctness
Avoid getter and setter methods, access the members directly instead.
```python
class Person:
    def __init__(self, name):
        self.name = name

        
person = Person('John Smith')
person.name = 'John William'  # accessing member variable directly
```

Only use built-in `property` decorator to achieve proper getter/setter functionality if it's justified.
```python
class Person:
    def __init__(self, name):
        self.name = name  # automatically calls setter
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = remove_non_ascii(name)


person = Person('John Smith')
person.name = 'John William'  # automatically calls setter
```
[More on that here](https://docs.quantifiedcode.com/python-anti-patterns/correctness/implementing_java-style_getters_and_setters.html)

### Code readability

### Anti-pattern
```python
l = [1, 2, 3]

# creating index variable
for i in range(0, len(l)):
    # using index to access list
    le = l[i]
    print(i, le)
```
### Best practice
```python
for i, le in enumerate(l):
    print(i, le)
```
[source](https://docs.quantifiedcode.com/python-anti-patterns/readability/using_an_unpythonic_loop.html?highlight=unpythonic)

# Security

## Use of `exec`
### Anti-pattern
```python
s = 'print(\'Hello, World!\')'
exec s
```
### Best practice
```python
def print_hello():
    print('Hello World!')

print_hello()
```

# Performance

## Using `key in list` to check if key is contained in list
### Anti-pattern
```python
l = [1, 2, 3, 4]

# iterates over three elements in the list
if 3 in l:
    print("The number 3 is in the list.")
else:
    print("The number 3 is NOT in the list.")
```
### Best practice
```python
s = set([1, 2, 3, 4])

if 3 in s:
    print("The number 3 is in the list.")
else:
    print("The number 3 is NOT in the list.")
```