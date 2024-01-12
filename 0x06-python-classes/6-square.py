#!/usr/bin/python3
"""empty class"""


class Square:
    """Empty clas"""

    def __init__(self, size=0, position=0):
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
            if isinstance(self.__position, tuple):
                for i in range(self.__position[1]):
                    print()
                
        else:
            flag =  self.__position

            if isinstance(self.__position, tuple):

                for i in range(flag[1]):
                    print()
                
            for i in range(self.__size):
                if isinstance(self.__position, tuple):

                    for _ in range(flag[0]):
                        print("_", end="")
                for _ in range(self.__size):
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
        if isinstance(position, tuple):
            flag = self.__position
            if isinstance(flag[0], int) and isinstance(flag[1], int):
                return self.__position
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @position.setter
    
    def position(self, position):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:

            if isinstance(position[0], int) and isinstance(position[1], int):
                self.__position = position
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
