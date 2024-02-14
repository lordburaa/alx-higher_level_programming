#!/usr/bin/python3
"""
    create class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """creating square class that inherit the Rectangle class"""
    nc_class = 0
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
        Square.nc_class += 1

    def __str__(self):
        return f"[Square] ({Square.nc_class}) {self.x}/{self.y} - {self.size}"

