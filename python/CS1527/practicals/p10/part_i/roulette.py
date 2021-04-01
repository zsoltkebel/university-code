# Date: 01/04/2021
#
# Given the following historical data on spins of a roulette wheel:
# spins = [('red', '18'), ('black', '13'), ('red', '7'),
#  ('red', '5'), ('black', '13'), ('red', '25'),
#  ('red', '9'), ('black', '26'), ('black', '15'),
#  ('black', '20'), ('black', '31'), ('red', '3')]
# We want to know how many red spins fall between each pair of black spins
# Write a generator function countReds(aList) that will yield the size of the gaps as it examines
# the spins.

spins = [('red', '18'), ('black', '13'), ('red', '7'),
         ('red', '5'), ('black', '13'), ('red', '25'),
         ('red', '9'), ('black', '26'), ('black', '15'),
         ('black', '20'), ('black', '31'), ('red', '3')]


def count_reds(spins):
    counter = 0
    for spin in spins:
        if spin[0] == 'red':
            counter += 1
        if spin[0] == 'black':
            yield counter
            counter = 0


if __name__ == '__main__':
    for gap in count_reds(spins):
        print(gap)
