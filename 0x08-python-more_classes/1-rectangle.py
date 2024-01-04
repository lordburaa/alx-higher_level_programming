#!/usr/bin/python3
"""Class created """

class Rectangle:
    """Empty rectangle"""
    
    def __init__(self, width=0, height=0):
        if isinstance(height, int):
            self.__height = height
        else:
            raise TypeError("height must be >= 0")
        if isinstance(widht, int):
            self.__width = width
        else:
            riase TypeError("width must be >= 0")
    
    @property
    def width(self):
        return self.width
    
    @property
    def height(self):
        return self.height

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

