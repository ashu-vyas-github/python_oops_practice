#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ashutosh

Class definition of Rectangle class used as a toy example for OOP concepts.

The Rectangle module contains the Rectangle class used as toy example to practice object-
oriented programming concepts. This will be updated throughout as new concepts are
learned and practiced.

OPTIONS ------------------------------------------------------------------
A description of each option that can be passed to this script.
(Placeholder for now, will be updated later.)

ARGUMENTS -------------------------------------------------------------
A description of each argument that can or must be passed to this script.
(Placeholder for now, will be updated later.)
"""


class Rectangle:
    """
    Class definition of Rectangle class used as a toy example for OOP concepts.

    The Rectangle module contains the Rectangle class used as toy example to practice object-
    oriented programming concepts. This will be updated throughout as new concepts are
    learned and practiced.

    OPTIONS ------------------------------------------------------------------
    A description of each option that can be passed to this script.
    (Placeholder for now, will be updated later.)

    ARGUMENTS -------------------------------------------------------------
    A description of each argument that can or must be passed to this script.
    (Placeholder for now, will be updated later.)
    """

    def __init__(self, length, width):
        """
        Rectangle class constructor method for object initialization.

        Constructor initialization method used and called upon creation of Rectangle object.

        Parameters
        ----------
        length : Float
            Length value of the longest side of the rectangle to be created.
            Eg: radius=3.5
        width : Float
            Width value of the shortest side of the rectangle to be created.
            Eg: width=1.5
        """
        self.length = length
        self.width = width


my_rectangle = Rectangle(length=10.5, width=7.5)
print("Object is at:", my_rectangle)
print("Length:", my_rectangle.length)
print("Width:", my_rectangle.width)
