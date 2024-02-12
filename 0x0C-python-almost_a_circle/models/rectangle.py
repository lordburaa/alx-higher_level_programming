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
    #Getter method
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    @setter.width
    def width(self, width)
        self.__width = width
    
    @setter.height
    def height(self, height)
        self.__height = height
    
    @setter.x
    def x(self, x)
        self.__x = x


    @setter.y
    def y(self, y)
        self.__y = y
