c = 3 * (10 ** 8)  # speed of light

seconds = float(input("seconds: "))

distance = seconds * c  # in meters

print("distance in meters:", distance)
print("distance in kilometers:", distance / 1000)
print("distance in miles:", distance * 0.621371)