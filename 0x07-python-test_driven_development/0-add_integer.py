#!/usr/bin/python3
"""new add
    integer two number
    two argument 
    must be an integer
"""


def add_integer(a, b=98):
    """doc
        Cheking the addition and change to int
        
        Args:
            a first argument
            b second argumet
    """

    if not isinstance(a, (int, float)) or a == None:
        raise ValueError("a must be an integer")
    if not isinstance(b, (int , float)) or b == None:
        raise ValueError("b must be an integer")
    
    return int(a) + int(b)