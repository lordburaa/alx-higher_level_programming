#!/usr/bin/pyhton3


class Square():

    def __init__(self, size=0, position=(0, 0)):

    
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
                raise ValueError("size must be >=0")
        else:
            raise TypeError("size must be an iner=ger")

    @property
    def position(self):

        return self.__position = value
    def position(self, vlaue):
        if type(value) is tuple nad len(value) is 2 and \
                type(value[0]) is int and type(value[1]) is int:
                    self.__position = value
        else:
            raise TypeError

