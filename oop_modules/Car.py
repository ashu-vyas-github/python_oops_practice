#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ashutosh

Class definition of Car class used as a toy example for OOP concepts.

The Car module contains the Car class used as toy example to practice object-
oriented programming concepts. This will be updated throughout as new concepts are
learned and practiced.

OPTIONS ------------------------------------------------------------------
A description of each option that can be passed to this script.
(Placeholder for now, will be updated later.)

ARGUMENTS -------------------------------------------------------------
A description of each argument that can or must be passed to this script.
(Placeholder for now, will be updated later.)
"""


class Car:
    """
    Class definition of Car class used as a toy example for OOP concepts.

    The Car module contains the Car class used as toy example to practice object-
    oriented programming concepts. This will be updated throughout as new concepts are
    learned and practiced.

    OPTIONS ------------------------------------------------------------------
    A description of each option that can be passed to this script.
    (Placeholder for now, will be updated later.)

    ARGUMENTS -------------------------------------------------------------
    A description of each argument that can or must be passed to this script.
    (Placeholder for now, will be updated later.)
    """

    def __init__(self, brand, model, year):
        """
        Car class constructor method for object initialization.

        Constructor initialization method used and called upon creation of Car object.

        Parameters
        ----------
        brand : String
            Brand name or company or manufacturer of the car.
            Eg: brand="Toyota"
        model : String
            Model name of the car.
            Eg: model="Camry"
        year : Int
            Year when the car model was launched to the general public.
            Positive valued integer, only include upto latest running year.
            Eg: year=2000
        """
        self.brand = brand
        self.model = model
        self.year = year


my_car = Car(brand="Porsche", model="911 Carrera", year=2020)
print("\nPassing arguments...")
print("Object is at:", my_car)
print("Brand:", my_car.brand)
print("Model:", my_car.model)
print("Year:", my_car.year)

my_car.year = 9999
print("\nModifying passed argument...")
print("Object is at:", my_car)
print("Brand:", my_car.brand)
print("Model:", my_car.model)
print("Year:", my_car.year)
