# Date: 01/04/2021
#
# Implement a Python iterator class PowerTwo the returns powers of 2, and demonstrate its use
# without using the “for i in PowerTwo() ...” format.

class PowerTwo:

    def __init__(self):
        self._base = 2
        self._exponent = 0

    def __next__(self):
        power = self._base ** self._exponent
        self._exponent += 1
        return power

    def __iter__(self):
        return self


if __name__ == '__main__':
    power_two = PowerTwo()
    iterator = iter(power_two)
    power = None

    while power is None or power <= 1024:
        power = next(iterator)
        print(power)
