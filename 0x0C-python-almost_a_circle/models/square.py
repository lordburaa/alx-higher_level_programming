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
        """str overiding the Rectangle class"""
        return f"[{self.__class__.__name__}] ({self.id})\
                {super().x}/{super().y} - {super().height}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update """
        list_t = ["id", "size", "x", "y"]
        if not kwargs:
            for i in range(len(args)):
                setattr(self, list_t[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """RETURN the dictionary representation fo Square
            The dictionary conatin:
                ->id
                ->size
                ->x
                ->y
        """
        to_dict = {"id": self.id, "x": self.x, "size": self.size, "y": self.y}

        return to_dict
