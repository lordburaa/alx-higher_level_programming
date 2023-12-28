#!/usr/bin/python3
"""empty class"""


class Square:
    """Empty clas"""

    def __init__(self, size=0):
        """Intialize """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """findig the area
         return the square of size
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif (self.__size < 0):
            raise ValueError("size must be >= 0")
        else:
            return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Set a new value"""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif (self.__size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
