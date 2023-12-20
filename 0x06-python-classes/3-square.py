#!/usr/bin/python3
"""empty square"""


class Square:
    """Represent square"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculate area
        return the sqare of the input"""
        return (self.__size) ** 2
