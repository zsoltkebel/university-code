# Author: Zsolt Kébel
# Date: 18/02/2021

class CircularArrayQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._storage = [None] * CircularArrayQueue.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            # TODO handle exception
            pass
        else:
            return self._storage[self._front]

    def enqueue(self, element):
        if self._size < len(self._storage):
            end = (self._front + self._size) % len(self._storage)
            self._storage[end] = element
            self._size += 1

    def dequeue(self):
        element = self._storage[self._front]
        self._storage[self._front] = None
        self._front = (self._front + 1) % len(self._storage)
        self._size -= 1
        return element
