#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ashutosh

Class definition of Backpack class used as a toy example for OOP concepts.

The Backpack module contains the Backpack class used as toy example to practice object-
oriented programming concepts. This will be updated throughout as new concepts are
learned and practiced.

OPTIONS ------------------------------------------------------------------
A description of each option that can be passed to this script.
(Placeholder for now, will be updated later.)

ARGUMENTS -------------------------------------------------------------
A description of each argument that can or must be passed to this script.
(Placeholder for now, will be updated later.)
"""


class Backpack:
    """
    Class definition of Backpack class used as a toy example for OOP concepts.

    The Backpack module contains the Backpack class used as toy example to practice object-
    oriented programming concepts. This will be updated throughout as new concepts are
    learned and practiced.

    OPTIONS ------------------------------------------------------------------
    A description of each option that can be passed to this script.
    (Placeholder for now, will be updated later.)

    ARGUMENTS -------------------------------------------------------------
    A description of each argument that can or must be passed to this script.
    (Placeholder for now, will be updated later.)
    """

    max_num_items = 10

    def __init__(self, items=[]):
        """
        Backpack class constructor method for object initialization.

        Constructor initialization method used and called upon creation of Backpack object.

        Parameters
        ----------
        items : List
            Items that are contained in the backpack. Initially, it is empty.
            Eg: items=["Pen", "Waterbottle", "Blanket"]
        """
        self.items = items


my_backpack = Backpack()
print("\nDefault argument...")
print("Object is at:", my_backpack)
print("List of items currently in the backpack:", my_backpack.items)

my_backpack = Backpack(items=["Waterbottle", "Pen", "Blanket"])
print("\nPassing argument...")
print("Object is at:", my_backpack)
print("List of items currently in the backpack:", my_backpack.items)

my_backpack.items = ["Book", "Map", "Wallet"]
print("\nModifying passed argument...")
print("Object is at:", my_backpack)
print("List of items currently in the backpack:", my_backpack.items)

print("\nBackpack class access class attribute:", Backpack.max_num_items)
print("my_backpack obect access class attribute:", my_backpack.max_num_items)

my_backpack = Backpack()
print("\nBefore modifying class attribute, default value declared inside class...")
print("Max items via class:", Backpack.max_num_items)
print("Max items via object:", my_backpack.max_num_items)

Backpack.max_num_items = 99
print("\nAfter modifying class attribute via class...")
print("Max items via class:", Backpack.max_num_items)
print("Max items via object:", my_backpack.max_num_items)

my_backpack.max_num_items = 666
print("\nAfter modifying class attribute via object...")
print("Max items via class:", Backpack.max_num_items)
print("Max items via object:", my_backpack.max_num_items)
