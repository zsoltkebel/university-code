from singly_linked_list import SinglyLinkedList


def delete_middle(node):
    while node._next._next is not None:
        node._value = node._next._value
        node = node._next
    node._next = None


if __name__ == '__main__':
    l = SinglyLinkedList()
    l.insert_first(1)
    l.insert_first(2)
    l.insert_first(3)
    l.insert_first(1)
    l.insert_first(3)
    l.insert_first(4)
    l.insert_first(1)
    l.insert_first(1)
    print(l)
    node = l._head._next._next
    delete_middle(node)

    print(l)
    i = 1

