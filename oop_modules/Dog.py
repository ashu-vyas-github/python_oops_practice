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

    def __init__(
        self, name="Rocky", age=3, breed="Labrador", social_security_code="89P13"
    ):
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
        social_security_code : String
            Alphanumeric code for the individual dog provided by the Federal government.
            Eg: social_security_code="89P13"
        """
        self.name = name
        self._age = age
        self.breed = breed
        self._social_security_code = social_security_code

    def get_social_security_code(self):
        return self._social_security_code

    def set_social_security_code(self, new_ssc):
        if isinstance(new_ssc, str) and new_ssc.isalnum():
            self._social_security_code = new_ssc
        else:
            print("Please enter a valid SSC consisting of only letters and numbers.")

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and (0 < new_age < 30):
            self._age = new_age
        else:
            print("Please enter a valid age value.")

    age = property(get_age, set_age)


my_dog = Dog()
print("\nDefault argument...")
print("Object is at:", my_dog)
print("Name of the dog:", my_dog.name)
print("Age of the dog:", my_dog.age, "y.o.")
print("Breed of the dog:", my_dog.breed)

my_dog = Dog(name="Mr. Buttons", age=5, breed="Collie", social_security_code="31P98")
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

print(f"\nSSC for {my_dog.name} is {my_dog.get_social_security_code()}")
my_dog.set_social_security_code(new_ssc="4L7D20")
print(f"New SSC is {my_dog.get_social_security_code()}")
my_dog.social_security_code = "9s5df6"
print(f"New SSC is {my_dog.get_social_security_code()}")
print(f"my_dog.social_security_code = {my_dog.social_security_code}")

my_dog = Dog(age=14)
print(my_dog.age)
print(my_dog._age)
print(my_dog.__dict__)
my_dog.age = 28
print(my_dog.age)
print(my_dog._age)
print(my_dog.__dict__)
