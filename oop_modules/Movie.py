#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ashutosh

Class definition of Movie class used as a toy example for OOP concepts.

The Movie module contains the Movie class used as toy example to practice object-
oriented programming concepts. This will be updated throughout as new concepts are
learned and practiced.

OPTIONS ------------------------------------------------------------------
A description of each option that can be passed to this script.
(Placeholder for now, will be updated later.)

ARGUMENTS -------------------------------------------------------------
A description of each argument that can or must be passed to this script.
(Placeholder for now, will be updated later.)
"""


class Movie:
    """
    Class definition of Movie class used as a toy example for OOP concepts.

    The Movie module contains the Movie class used as toy example to practice object-
    oriented programming concepts. This will be updated throughout as new concepts are
    learned and practiced.

    OPTIONS ------------------------------------------------------------------
    A description of each option that can be passed to this script.
    (Placeholder for now, will be updated later.)

    ARGUMENTS -------------------------------------------------------------
    A description of each argument that can or must be passed to this script.
    (Placeholder for now, will be updated later.)
    """

    uid_counter = 1

    def __init__(
        self,
        title="The Godfather",
        year=1972,
        language="English",
        rating=9,
        num_accidents=0,
    ):
        """
        Movie class constructor method for object initialization.

        Constructor initialization method used and called upon creation of Movie object.

        Parameters
        ----------
        title : String
            Title of the movie to be initialized.
            Eg: title="The Godfather"
        year : Int
            Year when the movie was released for general public in theaters.
            Must be positive valued number.
            Eg: year=1972
        language : String
            Original language in which the movie was released initially for general public.
            Eg: language="English"
        rating : Int
            User-rating of the movie between 0 and 10.
            Eg: rating=9
        num_accidents : Int
            Total number of accidents occured while making the film.
            Positive valued integer.
            Eg: num_accidents=3
        """
        self._uid = Movie.uid_counter
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating
        self._num_accidents = num_accidents

        Movie.uid_counter += 1

    def get_id(self):
        return self._uid

    @property
    def num_accidents(self):
        return self._num_accidents

    @num_accidents.setter
    def num_accidents(self, new_num_accidents=0):
        if isinstance(new_num_accidents, int) and new_num_accidents > 0:
            self._num_accidents = new_num_accidents
        else:
            print("Enter only valid number of accidents.")


my_movie = Movie()
print("\nDefault argument...")
print("Object is at:", my_movie)
print("Title:", my_movie.title)
print("Year:", my_movie.year)
print("Language:", my_movie.language)
print("Rating:", my_movie.rating)
# print("Movie id:", my_movie.uid)
print("Movie id:", my_movie._uid)

my_movie = Movie(title="Fantastic Four", year=2005, language="English", rating=9)
print("\nPassing argument...")
print("Object is at:", my_movie)
print("Title:", my_movie.title)
print("Year:", my_movie.year)
print("Language:", my_movie.language)
print("Rating:", my_movie.rating)
# print("Movie id:", my_movie.uid)
print("Movie id:", my_movie._uid)

my_movie = Movie(title="Fantastic Four", year=2005, language="English", rating=9)
my_movie.title = "Avengers: Endgame"
my_movie.year = 2019
my_movie.language = "English"
my_movie.rating = 10
print("\nModifying passed argument...")
print("Object is at:", my_movie)
print("Title:", my_movie.title)
print("Year:", my_movie.year)
print("Language:", my_movie.language)
print("Rating:", my_movie.rating)
# print("Movie id:", my_movie.uid)
print("Movie id:", my_movie._uid)

print("\nUsing getter method for id...")
print("The movie id via getter:", my_movie.get_id())

print("\nGetters and setters via property decorator...")
print(f"Number of accidents occured while filming: {my_movie.num_accidents}")
my_movie.num_accidents = 11
print(f"Updated number of accidents: {my_movie.num_accidents}")
