# Date: 01/04/2021
#
# Implement a Python class CountDown that takes a single integer parameter to its constructor and
# then behaves as an iterator – returning the next integer value in turn, counting down from the
# initial input value.

class CountDown:

    def __init__(self, num):
        self._start_from = num
        self._current_num = num

    def __next__(self):
        if self._current_num <= 0:
            raise StopIteration()

        num = self._current_num
        self._current_num -= 1
        return num

    def __iter__(self):
        return self


if __name__ == '__main__':
    cd = CountDown(4)
    for x in cd:
        print(x)
