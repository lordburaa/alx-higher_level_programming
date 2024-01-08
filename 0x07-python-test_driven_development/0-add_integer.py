#!/usr/bin/python3
"""new add
    integer two number
    two argument 
    must be an integer
"""


def add_integer(a, b=98):
    """doc
        Cheking the addition and change to int
    """
    flag = 0
    if not isinstance(a, (int, float)) or a == None:
        flag = 1
        raise ValueError("a must be an integer")
    else:
        a = int(a)
    if not isinstance(b, (int , float)) or b == None:
        raise ValueError("b must be an integer")
    else:
        b = int(b)
        if (flag == 0):
            return a + b
