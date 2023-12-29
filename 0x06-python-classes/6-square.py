#!/usr/bin/python3
"""empty class"""


class Square:
    """Empty clas"""

    def __init__(self, size=0, position=(0, 0)):
        """Intialize """
        """if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:"""
        self.__size = size
        self.__position = position

    def area(self):
        """findig the area
         return the square of size
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif (self.__size < 0):
            raise ValueError("size must be >= 0")
        else:
            return self.__size ** 2

    def my_print(self):
        """print the square"""
        print(self.pos_print(), end='')


    @property
    def size(self):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif (self.__size < 0):
            raise ValueError("size must be >= 0")
        else:
            return self.__size

    @size.setter
    def size(self, value):
        """Set a new value"""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif (self.__size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    @property
    def position(self):
        """if not isinstance(position, tuple) or self.__position[0] < 0 or self.__position[1] < 0 or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:"""
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in range(value):
            if not isinstance(value[i], int) or value[i] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = value

    def pos_print(self):
        """positin in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for i in range(self.position[1]):
            pos += "\n"
        for i in range(self.size):
            for k in range(self.position[0]):
                pos += " "
            for h in range(self.size):
                pos += "#"
            pos += "\n"
        return pos
