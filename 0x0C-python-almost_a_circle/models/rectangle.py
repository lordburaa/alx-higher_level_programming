#!/usr/bin/python3
"""
    inherit class
"""
from models.base import Base


class Rectangle(Base):
    """rectangle class  inherit `Base` class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """height setter method"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """x setter method"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """y setter method"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return the area of the retangel instance"""
        return self.__height * self.__width

    def display(self):
        """display the Rectangle instnace(area) using character #"""
        for _ in range(self.__height):
            for _ in range(self.__width):
                print("#", end="")
            print()
