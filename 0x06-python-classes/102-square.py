#!/usr/bin/python3
"""Defines a class square"""

class Square:
    """reperesents a square """
    def __init__(self, size=0):
        """itnitalize the square"""
        self.__size = size
    def area(self):
        """calculate the square"""
        return (self.__size) ** 2
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """ seter of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
    def __lt__(self, other):
        """compare > than sign"""
        return self.area() < other.area()

    def __le__(self, other):
        """ comare  less than sign"""
        return self.area() <= other.area()
    def __eq__(self, other):
        """compare if square is equal to another by arae"""
        return self.area() == other.area()
    def __ne__(self, other):
        """compare if square is not equal to anoehr by area"""
        return self.area() != other.area()
    def __ge__(self, other):
        """ compare is squae is greater tha or equal to another by are """
        return self.area() >= other.area()
    def __gt__(self, other):
        """compare is square i greaer than anoher by area"""
        return self.area() > other.area()
