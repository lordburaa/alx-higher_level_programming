#!/usr/bin/python3
""" Pascal """


def pascal_triangle(n):
    """pascal triangle"""
    tmp = [0]
    pascal_tr = []

    """if n <= 1:
        return pascal_tr
    """
    for i in range(1, n+1):
        tmp = add(tmp, i, n)
        pascal_tr.append(tmp)

    return pascal_tr


def add(old, n, size):
    """add the value side to each other  """
    list_new = []
    summ = 0
    if size <= 0:
        return list_new
    if len(old) == 1:
        old = [1, 1]
    else:
        for i in range(len(old) - 1):
            summ = old[i] + old[i + 1]
            list_new.append(summ)

    list_new.insert(0, 1)

    if n != 1:
        list_new.append(1)

    return list_new
