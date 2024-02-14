#!/usr/bin/python3
"""
    create class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """creating square class that inherit the Rectangle class"""

    nc_class = 0

    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of the child class inherit class Rectangle"""
        super().__init__(size, size, x, y, id)
        Square.nc_class += 1

    def __str__(self):
        return f"[Square] ({Square.nc_class}) {self.x}/{self.y} - {self.width}"

#    @property
#    def size(self):
#        return self.width
#
#    @size.setter
#    def size(self, size):
#        self.width = size
#        self.height = size
