#!/usr/bin/python3
"""

    This module has one functon

"""


def add_integer(a, b=98):
    """doc
        Cheking the addition and change to int
    """
    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer")
    if a is None:
        raise ValueError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise ValueError("b must be an integer")
    return int(a) + int(b)
