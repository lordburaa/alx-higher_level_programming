#!/usr/bin/python3
"""Define Magiclass """

import math

class MagicClass:
    """Represent circle"""
    def __intit__(self, radius=0):
        self.__radius = radius
    def area(self):
        """Calculates the area of the circle"""
        return (self.__radius ** 2) * math.pi
    def circumference(self):
        """ circumference of the circle"""
        return 2 * math.pi * self.__radius
