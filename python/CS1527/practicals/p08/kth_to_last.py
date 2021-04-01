
from singly_linked_list import SinglyLinkedList


def kth_to_last(k, singly_linked_list: SinglyLinkedList):
    kth = singly_linked_list._head
    end = singly_linked_list._head
    counter = 0
    while end is not None:
        if counter >= k:
            kth = kth._next
        end = end._next
        counter += 1
    return kth


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
print(kth_to_last(6, l))

print(l)
i = 1

