# wouldn't solve this task like this,
# it is solely for illustration for creating iterator
class CapitalIterable:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self


# using the iterator
iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')

# complex
iterator = iter(iterable)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

# all this is the same as
for i in iterable:
    print(i)
