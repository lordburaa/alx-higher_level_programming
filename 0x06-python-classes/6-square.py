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
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    if (self.__position[1] > 0):
                        print("_", end="")
                        continue
                    else:
                        print(" ", end="")
                for i in range(self.__size):
                    print('#', end="")
                print()
                

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
        if not isinstance(self.__position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(self.__position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
