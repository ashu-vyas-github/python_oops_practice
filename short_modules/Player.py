#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ashutosh

Class definition of Player class used as a toy example for OOP concepts.
"""


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, change=5):
        self.y += change

    def move_down(self, change=5):
        self.y -= change

    def move_right(self, change=2):
        self.x += change

    def move_left(self, change=2):
        self.x -= change


my_player = Player(5, 10)

my_player.move_up()
print(my_player.y)

my_player.move_up(8)
print(my_player.y)

my_player.move_down()
print(my_player.y)

my_player.move_down(3)
print(my_player.y)

my_player.move_right()
print(my_player.x)

my_player.move_right(1)
print(my_player.x)

my_player.move_left()
print(my_player.x)

my_player.move_left(10)
print(my_player.x)
