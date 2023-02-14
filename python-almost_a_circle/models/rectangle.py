#!/usr/bin/python3
"""
Module-rectangle
Contains class Rectangle
"""
from models.base import Base


class Rectangle(base):
    """
    Defines class rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
