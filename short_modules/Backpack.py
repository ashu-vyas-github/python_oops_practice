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

    def __init__(self, items=[], num_shoulder_straps=2):
        """
        Backpack class constructor method for object initialization.

        Constructor initialization method used and called upon creation of Backpack object.

        Parameters
        ----------
        items : List
            Items that are contained in the backpack. Initially, it is empty.
            Eg: items=["Pen", "Waterbottle", "Blanket"]
        num_shoulder_straps : Int
            Number of straps available to carry the bag on shoulder.
            Eg: num_shoulder_straps=2
        """
        self.items = items
        self._items = items
        self.__items = items
        self._num_shoulder_straps = num_shoulder_straps

    def get_items(self):
        return self._items

    def set_items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Enter a valid list type datatype of items.")

    items = property(get_items, set_items)

    @property
    def num_shoulder_straps(self):
        return self._num_shoulder_straps

    @num_shoulder_straps.setter
    def num_shoulder_straps(self, new_num_straps):
        if isinstance(new_num_straps, int) and new_num_straps > 0:
            self._num_shoulder_straps = new_num_straps
        else:
            print("Please enter a valid number of straps.")

    def add_item(self, new_item):
        if isinstance(new_item, str) and len(new_item) > 0:
            self._items.append(new_item)
        else:
            print("Please enter a valid string input.")

    def remove_item(self, rm_item):
        if rm_item in self._items:
            self._items.remove(rm_item)
        else:
            print("Error: Only a valid item can be removed from the list.")

    def has_item(self, ck_item):
        return ck_item in self._items

    def add_multiple_items(self, mult_items):
        for item in mult_items:
            self.add_item(item)


my_backpack = Backpack()
print("\nDefault argument...")
print("Object is at:", my_backpack)
print("List of items currently in the backpack:", my_backpack.items)
print("List of items currently in the backpack:", my_backpack._items)

my_backpack = Backpack(items=["Waterbottle", "Pen", "Blanket"])
print("\nPassing argument...")
print("Object is at:", my_backpack)
print("List of items currently in the backpack:", my_backpack.items)
print("List of items currently in the backpack:", my_backpack._items)

my_backpack.items = ["Book", "Map", "Wallet"]
print("\nModifying passed argument...")
print("Object is at:", my_backpack)
print("List of items currently in the backpack:", my_backpack.items)
print("List of items currently in the backpack:", my_backpack._items)

print("\nBackpack class access class attribute:", Backpack.max_num_items)
print("my_backpack obect access class attribute:", my_backpack.max_num_items)

my_backpack = Backpack(items=["Wrench", "Screwdriver", "Drill Machine"])
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

print("\nName mangling...")
print("List of items currently in the backpack:", my_backpack.items)
print("List of items currently in the backpack:", my_backpack._items)
# print("List of items currently in the backpack:", my_backpack.__items)
print("List of items currently in the backpack:", my_backpack._Backpack__items)

print("\nUsing getters and setters for items...")
print("Backpack items via getter:", my_backpack.get_items())
my_backpack.set_items(new_items=["Earphones", "Charger", "External HDD", "Laptop"])
print("Backpack items set via setter:", my_backpack.get_items())

print("\nGetters and setters via property decorator...")
print(f"Number of straps for the backpack: {my_backpack.num_shoulder_straps}")
my_backpack.num_shoulder_straps = 99
print(f"Updated number of straps: {my_backpack.num_shoulder_straps}")

print("\nAdd methods to class...")
my_backpack.add_item(new_item="Ruler")
my_backpack.add_item(new_item="Compass")
my_backpack.add_item(new_item="Notebook")
print("Updated list of items: ", my_backpack.items)
has_element = my_backpack.has_item(ck_item="Waterbottle")
if has_element is True:
    print("Backpack has Waterbottle.")
else:
    print("Backpack doesn't have Waterbottle.")
has_element = my_backpack.has_item(ck_item="Laptop")
if has_element is True:
    print("Backpack has Laptop.")
else:
    print("Backpack doesn't have Laptop.")

rm_im = "Earphones"
my_backpack.remove_item(rm_item=rm_im)
print(f"{rm_im} removed. Updated list: {my_backpack.items}")

my_backpack.add_multiple_items(mult_items=["Waterbottle", "Pen", "Pencil", "Eraser"])
print("Adding multiple items simultaneously. Updated list:", my_backpack.items)

print("\nUsing the id() function...")
print(f"The id of backpack object: {id(my_backpack)}")