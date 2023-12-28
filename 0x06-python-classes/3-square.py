#!/usr/bin/python3
"""empty class"""


class Square:
    """Empty clas"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    

    def area(self):
        """findig the area
         return the square of size
         """

        return self.__size * self.__size
