#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ashutosh

Class definition of Circle class used as a toy example for OOP concepts.

The Circle module contains the Circle class used as toy example to practice object-
oriented programming concepts. This will be updated throughout as new concepts are
learned and practiced.

OPTIONS ------------------------------------------------------------------
A description of each option that can be passed to this script.
(Placeholder for now, will be updated later.)

ARGUMENTS -------------------------------------------------------------
A description of each argument that can or must be passed to this script.
(Placeholder for now, will be updated later.)
"""


class Circle:
    """
    Class definition of Circle class used as a toy example for OOP concepts.

    The Circle module contains the Circle class used as toy example to practice object-
    oriented programming concepts. This will be updated throughout as new concepts are
    learned and practiced.

    OPTIONS ------------------------------------------------------------------
    A description of each option that can be passed to this script.
    (Placeholder for now, will be updated later.)

    ARGUMENTS -------------------------------------------------------------
    A description of each argument that can or must be passed to this script.
    (Placeholder for now, will be updated later.)
    """

    name = "Mr. Circle"

    def __init__(self, radius=3.5, color="Blue"):
        """
        Circle class constructor method for object initialization.

        Constructor initialization method used and called upon creation of Circle object.

        Parameters
        ----------
        radius : Float
            Radius of the circle to be created.
            Eg: radius=3.5
        color : String
            Color of the perimeter/boundary of the circle.
            Eg: color="Blue"
        """
        self._radius = radius
        self.color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0.0:
            self._radius = new_radius
        else:
            print("Please enter a valid value for radius.")

    radius = property(get_radius, set_radius)

    def calculate_diameter(self):
        self._diameter = 2 * self._radius
        print(f"The diameter of the circle: {self._diameter} units")
        return self._diameter


my_circle = Circle()
print("\nDefault argument...")
print("Object is at:", my_circle)
print("Radius:", my_circle.radius)
print("Color:", my_circle.color)

my_circle = Circle(radius=100, color="Red")
print("\nPassing argument...")
print("Object is at:", my_circle)
print("Radius:", my_circle.radius)
print("Color:", my_circle.color)

my_circle.radius = 999
my_circle.color = "Green"
print("\nModifying passed argument...")
print("Object is at:", my_circle)
print("Radius:", my_circle.radius)
print("Color:", my_circle.color)

print("\nBefore modifying class attribute, default value declared inside class...")
print("Name of the circle via class:", Circle.name)
print("Name of the circle via object:", my_circle.name)

Circle.name = "Mrs. Sphere"
print("\nAfter modifying class attribute via class...")
print("Name of the circle via class:", Circle.name)
print("Name of the circle via object:", my_circle.name)

my_circle.name = "Ms. Ring"
print("\nAfter modifying class attribute via object...")
print("Name of the circle via class:", Circle.name)
print("Name of the circle via object:", my_circle.name)

print("\nUsing getters and setters for radius...")
print("Circle radius via getter:", my_circle.get_radius())
my_circle.set_radius(new_radius=69.0)
print("Circle radius set via setter:", my_circle.get_radius())

print(f"\nCircle radius via property method: {my_circle.radius}")

print("\nAdd methods to class...")
my_circle.calculate_diameter()

print("\nUsing id() function...")
one_circle = Circle()
two_circle = Circle()
print(one_circle is two_circle)
print(one_circle == two_circle)