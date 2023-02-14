#!/usr/bin/python3
"""base model class."""


class Base:
    """
    The Base Class
    Attributes:
        __nb_object : private class atribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
