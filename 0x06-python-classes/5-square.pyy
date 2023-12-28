#!/usr/bin/python3
"""empty square"""


class Square:
    """Represent square"""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """calculate area
        return the sqare of the input"""
        if (self.__size == 0):
            print()
        for i in range(self.__size):
            for k in range(self.__size):
                print("#", end="")
            print()

    def my_print(self):
        """print the are"""
        self.area()

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
