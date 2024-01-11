#!/usr/bin/python3

""" moule containing that multiplies 2 matricies """


def matrix_mul(m_a, m_b):
    """ multiply two matrices """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")
