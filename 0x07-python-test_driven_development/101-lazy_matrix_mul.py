#!/usr/bin/python3
""" using numpy """


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplication of two array

        Args:
            m_a - matrix to be multiplied
            m_b - matrix to be multiplied

    """
    return np.matmul(m_a, m_b)
