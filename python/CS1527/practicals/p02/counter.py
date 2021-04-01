# Author: Zsolt Kébel
# Date: 03/02/2021

class Counter:

    object_count = 0
    increment_count = 0

    def __init__(self):
        self.count = 0

        Counter.object_count += 1

    def increment(self, count=1):
        self.count += count
        Counter.increment_count += 1

    def decrement(self, count=1):
        self.count -= count


counter = Counter()

counter.increment()
counter.decrement()

c2 = Counter()
c2.increment(3)
c2.increment()
c2.decrement()

print(Counter.object_count)
print(Counter.increment_count)

print(counter.count)
