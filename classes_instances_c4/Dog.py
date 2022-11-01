#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ashutosh

Class definition of Dog class used as a toy example for OOP concepts.

The Dog module contains the Dog class used as toy example to practice object-
oriented programming concepts. This will be updated throughout as new concepts are
learned and practiced.

OPTIONS ------------------------------------------------------------------
A description of each option that can be passed to this script.
(Placeholder for now, will be updated later.)

ARGUMENTS -------------------------------------------------------------
A description of each argument that can or must be passed to this script.
(Placeholder for now, will be updated later.)
"""


class Dog:
    """
    Class definition of Dog class used as a toy example for OOP concepts.

    The Dog module contains the Dog class used as toy example to practice object-
    oriented programming concepts. This will be updated throughout as new concepts are
    learned and practiced.

    OPTIONS ------------------------------------------------------------------
    A description of each option that can be passed to this script.
    (Placeholder for now, will be updated later.)

    ARGUMENTS -------------------------------------------------------------
    A description of each argument that can or must be passed to this script.
    (Placeholder for now, will be updated later.)
    """

    species = "Canis lupus"

    def __init__(self, name="Rocky", age=3, breed="Labrador"):
        """
        Dog class constructor method for object initialization.

        Constructor initialization method used and called upon creation of Dog object.

        Parameters
        ----------
        name : String
            Name of the dog.
            Eg: name="Rocky"
        age : Int
            Age of the dog in years.
            Positive valued integer number.
            Eg: age=3
        breed : String
            Breed of the dog.
            Eg: breed="Labrador"
        """
        self.name = name
        self.age = age
        self.breed = breed


my_dog = Dog()
print("\nDefault argument...")
print("Object is at:", my_dog)
print("Name of the dog:", my_dog.name)
print("Age of the dog:", my_dog.age, "y.o.")
print("Breed of the dog:", my_dog.breed)

my_dog = Dog(name="Mr. Buttons", age=5, breed="Collie")
print("\nPassing argument...")
print("Object is at:", my_dog)
print("Name of the dog:", my_dog.name)
print("Age of the dog:", my_dog.age, "y.o.")
print("Breed of the dog:", my_dog.breed)

my_dog.name = "Toughie"
my_dog.age = 9
my_dog.breed = "Pitbull"
print("\nModifying passed argument...")
print("Object is at:", my_dog)
print("Name of the dog:", my_dog.name)
print("Age of the dog:", my_dog.age, "y.o.")
print("Breed of the dog:", my_dog.breed)

print("\nClass attribute:", Dog.species)
