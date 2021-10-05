# Author: Zsolt Kébel
# Date: 11/02/2021

from shapes.shapes import Shape, Point, Rectangle, Circle, Cylinder



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
