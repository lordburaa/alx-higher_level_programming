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
    @setter.width
    def width(self, width):
        """width setter method"""
        self.__width = width

    @setter.height
    def height(self, height):
        """height setter method"""
        self.__height = height

    @setter.x
    def x(self, x):
        """x setter method"""
        self.__x = x

    @setter.y
    def y(self, y):
        """y setter method"""
        self.__y = y
