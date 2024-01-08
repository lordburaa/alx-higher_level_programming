#!/usr/bin/python3
"""same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """if the object is an instance of a class
    that inherite from inherit return true"""

    if issubclass(type(obj), a_class): 
        return True
    return False
