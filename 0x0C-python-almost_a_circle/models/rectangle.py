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
