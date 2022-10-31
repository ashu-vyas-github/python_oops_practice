#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ashutosh

Class definition of House class used as a toy example for OOP concepts.

The House module contains the House class used as toy example to practice object-
oriented programming concepts. This will be updated throughout as new concepts are
learned and practiced.

OPTIONS ------------------------------------------------------------------
A description of each option that can be passed to this script.
(Placeholder for now, will be updated later.)

ARGUMENTS -------------------------------------------------------------
A description of each argument that can or must be passed to this script.
(Placeholder for now, will be updated later.)
"""


class House:
    """
    Class definition of House class used as a toy example for OOP concepts.

    The House module contains the House class used as toy example to practice object-
    oriented programming concepts. This will be updated throughout as new concepts are
    learned and practiced.

    OPTIONS ------------------------------------------------------------------
    A description of each option that can be passed to this script.
    (Placeholder for now, will be updated later.)

    ARGUMENTS -------------------------------------------------------------
    A description of each argument that can or must be passed to this script.
    (Placeholder for now, will be updated later.)
    """

    def __init__(self, price):
        """
        House class constructor method for object initialization.

        Constructor initialization method used and called upon creation of House object.

        Parameters
        ----------
        price : Float
            Price of the house with decimal places.
            Eg: price=250000.42
        """
        self.price = price


my_house = House(price=500000)
print(my_house)
