#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ashutosh

Exercise example for getter, setter, property, decorator.
"""


class BouncyBallFunc:
    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if isinstance(new_price, float) and new_price > 0.0:
            self._price = round(new_price, 2)
        else:
            print("Enter valid price value.")

    price = property(get_price, set_price)

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if isinstance(new_size, int) and (0 < new_size < 10):
            self._size = new_size
        else:
            print("Enter valid size value between 1 to 9.")

    size = property(get_size, set_size)

    def get_brand(self):
        return self._brand

    def set_brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.isalpha():
            self._brand = new_brand
        else:
            print("Enter valid price value.")

    brand = property(get_brand, set_brand)


class BouncyBallDeco:
    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float) and new_price > 0.0:
            self._price = round(new_price, 2)
        else:
            print("Enter valid price value.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if isinstance(new_size, int) and (0 < new_size < 10):
            self._size = new_size
        else:
            print("Enter valid size value between 1 to 9.")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.isalpha():
            self._brand = new_brand
        else:
            print("Enter valid price value.")


ball_func = BouncyBallFunc(price=10.99, size=4, brand="Adidas")
print("\n\nObject initialization for property methods...")
print(f"Price: {ball_func.get_price()}")
print(f"Size: {ball_func.get_size()}")
print(f"Brand: {ball_func.get_brand()}")
print("Modifying attributes using property methods...")
ball_func.set_price(new_price=999.99)
ball_func.set_size(new_size=1)
ball_func.set_brand(new_brand="FIFA")
print(f"Price: {ball_func.get_price()}")
print(f"Size: {ball_func.get_size()}")
print(f"Brand: {ball_func.get_brand()}")

ball_deco = BouncyBallDeco(price=29.99, size=7, brand="Reebok")
print("\n\nObject initialization for decorators...")
print(f"Price: {ball_deco.price}")
print(f"Size: {ball_deco.size}")
print(f"Brand: {ball_deco.brand}")
print("Modifying attributes using decorators...")
ball_deco.price = 79.99
ball_deco.size = 9
ball_deco.brand = "Nike"
print(f"Price: {ball_deco.price}")
print(f"Size: {ball_deco.size}")
print(f"Brand: {ball_deco.brand}")
