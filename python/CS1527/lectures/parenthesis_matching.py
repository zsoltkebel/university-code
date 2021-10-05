# Author: Zsolt Kébel
# Date: 13/02/2021

# CS1527 Lecture 3.4

import array_stack

d = array_stack.ArrayStack()


def is_matching(expr):
    s = array_stack.ArrayStack()

    lefty = '({['
    righty = ')}]'
    for i in expr:
        if lefty.__contains__(i):
            s.push(i)
        elif righty.__contains__(i):
            if s.is_empty():
                return False
            elif lefty.index(s.pop()) != righty.index(i):
                return False

    return s.is_empty()


print(is_matching('([[]](){}())'))
print(is_matching('([[](){}())'))
print(is_matching('([[]](){}()'))
