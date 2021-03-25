class SinglyLinkedList:
    """A base class providing a singly linked list representation"""

    class _Node:

        def __init__(self, element, next):
            self._value = element
            self._next = next

        def __str__(self):
            return str(self._value)

    def __init__(self):
        self._head = None
        self._size = 0

    def __str__(self):
        s = ''
        node = self._head
        while node is not None:
            s += str(node._value)
            s += ', '
            node = node._next
        return s

    def insert_first(self, value):
        node_new = self._Node(value, self._head)
        self._head = node_new

    def insert_last(self, value):
        node_new = self._Node(value, None)

        last_node = self._head
        while last_node._next is not None:
            last_node = last_node._next

        last_node._next = node_new

    def remove(self, node):
        """Delete nonsentinel node from the list and return its element."""
        current_node = self._head
        while current_node._next is not None and current_node._next != node:
            current_node = current_node._next

        current_node._next = node._next
        node._next = node._value = None


# s = SinglyLinkedList()
# s.insert_first(1)
# s.insert_first(2)
# s.insert_first(3)
# s.insert_first(4)
