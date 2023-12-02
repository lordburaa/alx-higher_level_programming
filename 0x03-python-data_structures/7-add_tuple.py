#!/usr/bin/python3
def add_tuple(tuple_a =(), tuple_b = ()):
    leng_a = len(tuple_a)
    leng_b = len(tuple_b)
    if (leng_a == 1):
        tuple_a = (tuple_a[0], 0,)

    if (leng_a == 0):
        tuple_a = (0, 0,)

    if (leng_b == 1):
        tuple_b = (tuple_b[0], 0,)

    if (leng_b == 0):
        tuple_b = (0, 0,)

    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1],)
    return tuple_c
