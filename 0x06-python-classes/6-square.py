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
        if self.__size > 0:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print("_", end="")

                    print("#" * self.__size)

                print()
    def my_print(self):
        """print the are"""
        for i in range(self.__position[1]):
            print()
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
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2 and \
                type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__poisition = value
        else:
                    raise TypeError("position must be a tuple of 2 positive integers")

    """print with new line """
