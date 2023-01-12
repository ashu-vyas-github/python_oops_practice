#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ashutosh

Mini project of bugs fixing exercise.

Resolve the typos and bugs in the below example:

class Donut
        def _ini__(flavor, toppings, filling, size):
                self.flavor = flavor
                self.toppings = toppings
                self.filling = filling
                size = self.size

class Customer:

	def _init_(self, name, age address, favorite_dessert)
		self.name = name
		self.age = age
		self.address = address
		favorite_dessert = self.favorite_dessert

Cake:
	__init__(self, flavor, price, quality):
		self.flavor = flavor
		self.price = price
		self.quality = quality

"""


class Donut:
    def __init__(self, flavor, toppings, filling, size):
        self.flavor = flavor
        self.toppings = toppings
        self.filling = filling
        self.size = size


class Customer:
    def __init__(self, name, age, address, favorite_dessert):
        self.name = name
        self.age = age
        self.address = address
        self.favorite_dessert = favorite_dessert


class Cake:
    def __init__(self, flavor, price, quality):
        self.flavor = flavor
        self.price = price
        self.quality = quality
