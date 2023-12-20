#!/usr/bin/python3
"""empty square"""


class Square:
    """Represent square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        """calculate area
        return the sqare of the input"""
        if (self.__size == 0):
            print()
        for i in range(self.__size):
            for i in range(self.position[0]):
                print("_", end="")
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 postive integers")
        else:
            if position[0]  is not int:
                raise TypeError("position must be a tuple of 2 positive integers")
                
            self.__position = position
    """print with new line """
