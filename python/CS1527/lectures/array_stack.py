# Author: Zsolt Kébel
# Date: 13/02/2021

# CS1527 Lecture 3.4

class ArrayStack:
    """LIFO stack implementation using Python List"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    """Add element e to the top of stack S."""
    def push(self, element):
        self._data.append(element)

    """Remove and return the top element from the stack S;
    an error occurs if the stack is empty."""
    def pop(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        else:
            return self._data.pop()

    def __str__(self):
        return str(self._data)
