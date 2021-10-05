# Testing Multiple User Input in Python 3
###### What to do when you need to test a sequence of inputs to console in Python?

The `return_value` configures the value returned when the mock is called. It will always return the same value when the mock is called.

The `side_effect` argument can accept a function to be called when the mock is called, an iterable or an Exception.
By passing in an iterable we can mock multiple inputs inside the testing function,
because it will yield the next value everytime it’s called.
```python
import unittest
from unittest.mock import patch    


class Test(unittest.TestCase):
    
    @patch('builtins.input', return_value=10)
    def test_using_return_value(self, mock_input):
        calling_1 = mock_input()
        calling_2 = mock_input()
        self.assertTrue(calling_1 == 10 and calling_2 == 10)

    @patch('builtins.input', side_effect=['First', 'Second', 'Third'])
    def test_using_side_effect(self, mock_input):
        calling_1 = mock_input()  # = 'First'
        calling_2 = mock_input()  # = 'Second'
        calling_3 = mock_input()  # = 'Third'
        self.assertTrue(calling_1 == 'First' and calling_2 == 'Second' and
                        calling_3 == 'Third')
```

## Example
sum.py:
```python
def sum():
    """Asks for the number of integers the user will type and
    the space separated integers."""
    n = input("Type the number of integers: ")
    L = input("Type the integers separated by space: ")
    L = L.split(' ')
    result = 0
    for num in range(n):
        result += int(L[num])
    return result
```
test_sum.py:
```python
import unittest
from unittest.mock import patch

from sum import sum

class TestListSum(unittest.TestCase):

    string_of_ints = '1 2 3 4 5'

    string_of_ints_2 = '1 1 1 1 1 1 1 1 1 1'

    @patch('builtins.input', side_effect=[5, string_of_ints])
    def test_sum_string_of_ints(self, mock_inputs):
        result = sum()
        self.assertEqual(result, 15)

    @patch('builtins.input', side_effect=[10, string_of_ints_2])
    def test_sum_string_of_ints_2(self, mock_inputs):
        result = sum()
        self.assertEqual(result, 10)
```
## Further reading
- [Andressa Cabistani - Testing inputs in Python3](https://andressa.dev/2019-07-20-using-pach-to-test-inputs/)
- [stackoverflow - Using unittest.mock to patch input() in Python 3](https://stackoverflow.com/questions/18161330/using-unittest-mock-to-patch-input-in-python-3)
- [unittest.mock - return_value](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value)
- [unittest.mock - side_effect](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect)
- [Lisa Roach - Demystifying the Patch Function - PyCon 2018](https://www.youtube.com/watch?v=ww1UsGZV8fQ)
