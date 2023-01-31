#!/usr/bin/python3
"""
Module 0-square
Defines class Square
"""


class Square:
    """Empty class"""
    def __init__(self, size=0):
        """Initializes the data."""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size)**2
