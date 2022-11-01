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
        self.radius = radius
        self.color = color


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
