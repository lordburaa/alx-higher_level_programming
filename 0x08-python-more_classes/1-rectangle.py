#!/usr/bin/python3
"""Class created """

class Rectangle:
    """Empty rectangle"""
    
    def __init__(self, width=0, height=0):
        if not isinstance(height, int) or  height < 0:
            raise TypeError("height must be >= 0")
        self.__height = height
        if not isinstance(width, int) or width < 0:
            raise TypeError("width must be >= 0")
        self.__width = width
           
    
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

