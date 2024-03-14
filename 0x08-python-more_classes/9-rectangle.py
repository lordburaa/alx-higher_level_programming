#!/usr/bin/python3
"""class that defines a rectangle"""


class Rectangle:
    """this represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """initalizing this rectangel clas
        args:
            width represent width of the rectangle
            height: represents the height ofth erectnalge

        Raises:
            TypeError: is size is not intege
            ValueError: is size is less than zeo
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instnaces += 1

    @property
    def width(self):
        """retrives width attribute"""
        return self.__width

    @widht.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            """retirves height attribute"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets height attribute"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height=  value

        def area(self):
            """return  the perimeter of the rectangle"""
            if self.__width == 0 or self.__height = 0:
                return (0)
            return ((self.__widht * 2) + (self.__height * 2))

        def __str__(self) -> str:
            """presents a diagram of the recctangle defined for an obejct"""
        
