#!/usr/bin/python3
"""
    create class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """creating square class that inherit the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of the child class inherit class Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({super().id}) {super().x}/{super().y} - {super().width}"

#    @property
#    def size(self):
#        return self.width
#
#    @size.setter
#    def size(self, size):
#        self.width = size
#        self.height = size
