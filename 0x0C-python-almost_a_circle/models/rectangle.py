#!/usr/bin/python3
"""
    inherit class
"""
from models.base import Base


class Rectangle(Base):
    """rectangle class  inherit `Base` class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    # Getter method
    @property
    def width(self):
        """width attribute"""
        return self.__width

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @property
    def y(self):
        """y getter method"""
        return self.__y

    # setter method for attribute
    @width.setter
    def width(self, width):
        """width setter method"""
        if not is isinstance(width, int):
            raise TypeError(f"{width} must be an integer")
        if width <= 0:
            raise ValueError(f"{width} must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """height setter method"""
        if not is isinstance(height, int):
            raise TypeError(f"{height} must be an integer")
        if height <= 0:
            raise ValueError(f"{height} must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """x setter method"""
        if not is isinstance(x, int):
            raise TypeError(f"{x} must be an integer")
        if x < 0:
            raise ValueError(f"{x} must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """y setter method"""
        if not is isinstance(y, int):
            raise TypeError(f"{y} must be an integer")
        if y < 0:
            raise ValueError(f"{y} must be >= 0")
        self.__y = y
