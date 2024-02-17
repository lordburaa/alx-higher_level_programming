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

    def __str__(self):
        """str method"""
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                self.id, self.__x, self.__y, self.__width, self.__height))
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
        x = [' ' * self.__x]
        y = ['\n' * (self.__y - 1)]

        char = ['#' * self.__width for _ in range(self.__height)]
        # changing the x list to char
        x_join = ''.join(x)
        # join the char and string x_join
        x_char = [x_join + i for i in char]
        # join the end of every char in the list with new line
        display = '\n'.join(x_char)
        if self.__y != 0:
            print(''.join(y))
        print(display)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        list_t = ["id", "width", "height", "x", "y"]
        if not kwargs:
            for i in range(len(args)):
                setattr(self, list_t[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return the dictionary representation of retangle"""
        obj_dic = {'id': self.id, 'width': self.width,
                   'height': self.height, 'x': self.x, 'y': self.y}

        return obj_dic
