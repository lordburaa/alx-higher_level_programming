#!/usr/bin/pyhton3
""" square module 
  """
class Square():
    """Define square"""
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
            raise TypeError("size must be an iner=ger")

    @property
    def position(self):

        return self.__position
    def position(self, vlaue):
        if type(value) is tuple and len(value) is 2 and \
                type(value[0]) is int and type(value[1]) is int:
                    self.__position = value
        else:
            raise TypeError("position must be tuple of 2 positive integers")
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
