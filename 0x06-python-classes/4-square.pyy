#!/usr/bin/python3
"""empty square"""


class Square:
    """Represent square"""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """calculate area
        return the sqare of the input"""
        return (self.__size) ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size nust be >= 0")
            else:
                self.__size = value
