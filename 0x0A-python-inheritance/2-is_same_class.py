#!/usr/bin/python3
"""checking the class"""


def is_same_class(obj, a_class):
    """REturn true if the object is an instance of the specified class"""

    if isinstance(obj, a_class):
        if (type(obj) == a_class):
            return True
    return False
