"""Class created """

class Rectangle:
    """Empty rectangle"""
    
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
    
    def __str__(self):
        c = ""
        for i in range(self.__height):
            for _ in range(self.__width):
                c += '#'
            if (i != self.__height - 1):
                c += '\n'
        return c


    def perimeter(self):
        return 2*(self.__height + self.__width)
    def area(self):
        return self.__height * self.__width

    @property
    def width(self):
        return self.width
    
    @property
    def height(self):
        return self.height

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

