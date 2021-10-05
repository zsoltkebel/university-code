# Author: Zsolt Kébel
# Date: 07/10/2020

# Write a program that tells the user the exact coinsNeeded in British coins. For example:
# [] If the user entered (73), the result should be:
# “You will receive 1 50p coin, 1 20p coin, 1 2p coin and 1 1p coin.
# [] If thee user entered (424) the result should be:
# “You will receive 2 2pounds coin, 1 20p coin and 2 2p coin.
# Etc..

pence = int(input("Pence: "))
coins = [200, 100, 50, 20, 10, 5, 2, 1]  # theoretically 200 pence = 2 pounds and 100 pence = 1 pound

# number of coins needed
coinsNeeded = [0, 0, 0, 0, 0, 0, 0, 0]  # x200 x100 x50 x20 x10 x5 x2 x1 respectively

print("You get ...")

currentAmount = pence

for i in range(len(coins)):
    if currentAmount // coins[i] > 0:
        coinsNeeded[i] += currentAmount // coins[i]  # store number of coins needed in array
        currentAmount = currentAmount % coins[i]

        if coins[i] >= 100:
            print(coinsNeeded[i], "x ", coins[i] // 100, " pounds coin", sep="")
        else:
            print(coinsNeeded[i], "x ", coins[i], " pence coin", sep="")
