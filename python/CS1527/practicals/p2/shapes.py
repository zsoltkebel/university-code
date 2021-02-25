# Author: Zsolt Kébel
# Date: 03/02/2021

import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x_coord(self):
        return self.x

    def get_y_coord(self):
        return self.y

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"Point(x:{self.x},y:{self.y})"


class Shape:

    def __init__(self, colour, centre):
        self.colour = colour
        self.centre = centre

    def get_colour(self):
        return self.colour


class Rectangle(Shape):

    def __init__(self, colour, width, length, centre):
        super().__init__(colour, centre)

        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return self.width * 2 + self.length * 2

    def __str__(self):
        return f"Rectangle: {self.width}x{self.length}"


class Circle(Shape):

    def __init__(self, colour, radius, centre):
        super().__init__(colour, centre)

        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_radius(self):
        return self.radius

    def __str__(self):
        return f"Circle: radius: {self.radius}"


class Cylinder:

    def __init__(self, base: Circle, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 2 * math.pi * self.base.radius * self.height + 2 * math.pi * (self.base.radius ** 2)

    def get_volume(self):
        return math.pi * (self.base.radius ** 2) * self.height

    def __str__(self):
        return f"Cylinder: radius: {self.base.radius}, height: {self.height}"


def test_shapes():
    shape = Shape("red", Point(2.0, 4.0))
    rect = Rectangle("blue", 3.4, 2.0, Point(2.0, 4.0))
    circle = Circle("yellow", 4.5, Point(2.0, 4.0))
    cylinder = Cylinder(Circle("green", 4.5, Point(2.0, 4.0)), 4.0)

    print(shape.get_colour())

    print(rect)
    print(circle)
    print(cylinder)

    print(cylinder.base.centre.distance_from_origin())


test_shapes()
