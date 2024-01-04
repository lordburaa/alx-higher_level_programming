#!/usr/bin/python3
"""Class created """


class Rectangle:
    """Empty rectangle"""

    def __init__(self, width=0, height=0):
        """Initializeation of widht and height"""

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self):
        """Return width"""
        return self.__width

    @property
    def height(self):
        """Return height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setting width"""
        if not isinstance(value, int) or value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """seting height"""
        if not isinstance(value, int) or value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
