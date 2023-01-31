#!/usr/bin/python3
"""
Module 0-square
Defines class Square
"""


class Square:
    """Empty class"""
    def __init__(self, size=0):
        """Initializes the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        return (self.__size)**2
