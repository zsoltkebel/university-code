
from singly_linked_list import SinglyLinkedList


def remove_duplicates(singly_linked_list: SinglyLinkedList):
    buffer = set()

    prev_node = None
    current_node = singly_linked_list._head
    while current_node is not None:
        if prev_node is not None and current_node._value in buffer:
            # delete node
            prev_node._next = current_node._next
            current_node._next = current_node._value = None  # deprecate Node
            current_node = prev_node
            # singly_linked_list.remove(current_node)
        else:
            buffer.add(current_node._value)

        prev_node = current_node
        current_node = current_node._next


def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return ll

def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return ll


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
remove_duplicates(l)

print(l)
i = 1

