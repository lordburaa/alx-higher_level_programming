#!/usr/bin/python3
"""
    square
"""


def print_square(size):
    """ 
        print square
    """
    if type(size) != int:
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size > 0 :
        for i in range(size):
            for _ in range(size):
                print("#", end="")
            print()

