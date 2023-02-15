#!/usr/bin/python3
"""
Module-rectangle
Contains class Rectangle
"""
from .base import Base


class Rectangle(Base):
    """
    Defines class rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            Width Getter
        """
        return self.__width

    @property
    def height(self):
        """
            height Getter
        """
        return self.__height

    @property
    def x(self):
        """
            x Getter
        """
        return self.__x

    @property
    def y(self):
        """
            y Getter
        """
        return self.__y

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
