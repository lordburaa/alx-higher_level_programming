#!/usr/bin/pyhton3
""" square module 
  """
class Square():
    """Define square"""

    def __str__(self):
        """teach oython to print thesquare my way"""
        return self.pos_print()[:-1]
    def __init__(self, size=0, position=(0, 0)):
        self.size =size
        self.position = position

    
    def __str__(self):
        square_str = ""
        if self.__size > 0:
            for y in range(self.__position[1]):
                square_str += '\n'
            for x in range(self.__size):
                square_str += ' ' * self.__position[0]
                square_str += '#' * self.__size + '\n'
        return square_str[:-1]

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >=0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an inerger")

    @property
    def position(self):
        return self.__position
    def position(self, vlaue):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value 
    def area(self):
        """return the current square area"""
        return self.__size ** 2
    def my_print(self):
        """prints the square with the # character on stdout """
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__positoin[0], end='')
                print('#' * self.__size)
        else:
            print()
