#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = [[row[i] * row[i] for row in matrix] for i in range(3)]

    return new
#   return [[x*x for x in line] for line in matrix]
