# Author: Zsolt Kébel
# Date: 08/10/2020

# The amount of energy required to increase the temperature of one gram
# of a material by one degree Celsius is the material’s specific heat capacity, C.
# The total amount of energy required to raise m grams of a material by ΔT degrees
# Celsius can be computed using the formula:
#
# q = mCΔT.
#
# Write a program that reads the mass of some water and the temperature coinsNeeded from the user.
# Your program should display the total amount of energy that must be added or removed to achieve the desired
# temperature coinsNeeded.
#
# Extend your program so that it also computes the cost of heating the water.
# Electricity is normally billed using units of kilowatt hours rather than Joules.
# In this exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour.
# Use your program to compute the cost of boiling water for a cup of coffee.

cWater = 4182  # approximately https://en.wikipedia.org/wiki/Specific_heat_capacity

mass = int(input("Mass of water: "))
tempChange = int(input("Temperature coinsNeeded: "))

energyJoules = mass * cWater * tempChange

print(energyJoules, "Joules energy")

energyKilowattHour = energyJoules / 3600000
cost = energyKilowattHour * 8.9

print(cost, "cents")
