# Author: Zsolt Kébel
# Date: 04/11/2020

import random

rand1 = random.randint(0, 999)
rand2 = random.randint(0, 999)

guess = int(input("Guess: "))

while guess != rand1 + rand2:
    guess = int(input("Guess: "))

print("Congratulate!")
