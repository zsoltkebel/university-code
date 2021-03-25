class DoublyLinkedList:

    class _Node:

        def __init__(self, prev_e, next_e, value):
            self._prev_e = prev_e
            self._next_e = next_e
            self._value = value

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next_e = self._trailer
        self._trailer._prev_e = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def insert_between(self, predecessor: _Node, successor: _Node, value):
        node_new = self._Node(predecessor, successor, value)
        predecessor._next_e = node_new
        successor._prev_e = node_new
        self._size += 1

    def delete(self, node: _Node):
        predecessor = node._prev_e
        successor = node._next_e
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        value = node._value  # record deleted value
        node._prev_e = node._next_e = node._value = None  # deprecate node
        return value

