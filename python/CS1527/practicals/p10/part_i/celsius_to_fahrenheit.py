# Date: 01/04/2021
#
# 3.(a)
# Use a Python list comprehension to convert the following list of temperatures in degrees
# Celsius to the equivalent values on the Fahrenheit temperature scale.
# celsius_t = [39.2, 36.5, 37.3, 37.8]
# Note: The formula for converting between the two scales is:
# degrees F = (9/5 x degrees C) + 32
#
# 3.(b)
# Write a list comprehension that generates the Pythagorean triples for values of x, y, z less
# than 30. [A Pythagorean triple is one for which x2 + y2 = z2]
#
# 4.
# Write a Python set comprehension to compute the set of double digit odd integers.

if __name__ == '__main__':
    # 3.(a)
    celsius_t = [39.2, 36.5, 37.3, 37.8]
    fahrenheit_t = [((9/5) * celsius_value) + 32 for celsius_value in celsius_t]
    print(celsius_t)
    print(fahrenheit_t)

    # 3.(b)
    pythagorean_triples = [(x, y, z) for x in range(1, 30) for y in range(1, 30) for z in range(1, 30)
                           if x ** 2 + y ** 2 == z ** 2]
    print(pythagorean_triples)

    # 4.
    double_odd = {num for num in range(10, 100) if num % 2 == 1}
    print('Double digit odd integers: ', double_odd)
