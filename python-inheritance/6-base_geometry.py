#!/usr/bin/python3
"""initializate module"""


class BaseGeometry:
    """create class"""
    @property
    def area(self):
        raise Exception("area() is not implemented")
