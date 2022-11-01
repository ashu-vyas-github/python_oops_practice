#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ashutosh

Class definition of Pizza class used as a toy example for OOP concepts.

The Pizza module contains the Pizza class used as toy example to practice object-
oriented programming concepts. This will be updated throughout as new concepts are
learned and practiced.

OPTIONS ------------------------------------------------------------------
A description of each option that can be passed to this script.
(Placeholder for now, will be updated later.)

ARGUMENTS -------------------------------------------------------------
A description of each argument that can or must be passed to this script.
(Placeholder for now, will be updated later.)
"""


class Pizza:
    """
    Class definition of Pizza class used as a toy example for OOP concepts.

    The Pizza module contains the Pizza class used as toy example to practice object-
    oriented programming concepts. This will be updated throughout as new concepts are
    learned and practiced.

    OPTIONS ------------------------------------------------------------------
    A description of each option that can be passed to this script.
    (Placeholder for now, will be updated later.)

    ARGUMENTS -------------------------------------------------------------
    A description of each argument that can or must be passed to this script.
    (Placeholder for now, will be updated later.)
    """

    price = 12.99

    def __init__(
        self,
        description="Marghareita",
        toppings=["Tomato sauce", "Mozzarella", "Cheddar"],
        crust="New York style",
    ):
        """
        Pizza class constructor method for object initialization.

        Constructor initialization method used and called upon creation of Pizza object.

        Parameters
        ----------
        description : String
            Name of the pizza as per the menu.
            Eg: description="Marghareita"
        toppings : List
            Toppings to be added on the base, sauce and toppings both.
            List of string elements.
            Eg: toppings=["Tomato sauce", "Mozzarella", "Cheddar"]
        crust : String
            Type and style of crust.
            Eg: crust="New York style"
        """
        self.description = description
        self.toppings = toppings
        self.crust = crust


my_pizza = Pizza()
print("\nBefore modifying class attribute, default value declared inside class...")
print("Price of the pizza via class:", Pizza.price)
print("Price of the pizza via object:", my_pizza.price)

Pizza.price = 99.99
print("\nAfter modifying class attribute via class...")
print("Price of the pizza via class:", Pizza.price)
print("Price of the pizza via object:", my_pizza.price)

my_pizza.price = 999.99
print("\nAfter modifying class attribute via object...")
print("Price of the pizza via class:", Pizza.price)
print("Price of the pizza via object:", my_pizza.price)
