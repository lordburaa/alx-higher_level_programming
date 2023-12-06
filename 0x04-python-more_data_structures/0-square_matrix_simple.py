#!/bin/python3
def square(new):
    temp = []
    if (type(new) == int):
        return (new * new)
    
    for i in new:
        temp.append(i*i)
    return (temp)


def square_matrix_simple(matrix=[]):
    new = list(map(square, matrix))
    return new
