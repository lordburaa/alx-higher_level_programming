#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """matrix multiplication"""

    row2 = len(m_b)
    row1 = len(m_a)
    col1 = 0
    cap = 0

    #checking the matrix if empty
    for i in m_a:
        if len(i) == 0:
            raise TypeError("m_a can't be empty")

    if len(m_a) == 0:
        raise TypeError("m_a can't be empty")



    for i in m_b:
        if len(i) == 0:
            raise TypeError("m_b can't be empty")

    if len(m_b) == 0:
        raise TypeError("m_b can't be empty")
#checking the int or float if it contain
    








    for check_col in m_a:
        col1 = len(check_col)

    out = 1

    for check in m_a:
        if len(check) != col1:
            out = 0
            break

    if (out == 0):
        print("the leng is not the same for the secnt matrix")
        exit()
    for i in m_b:
        col2 = len(i)
        break

    for flag in m_b:
        if len(flag) == col2:

            cap = 1
            continue
        else:
            cap = 0
            break
    if cap == 0:
        print(" the column are not the same ")
        exit()
    if  (row2 != col1):
        print("multiplication of the row by colmn is imporsible")
        exit()

    if cap == 1 and row2 == col1:

        mul_arr = [[0] * col2 for _ in range(row1)]

        for i in range(row1):
            for k in range(col2):
                for j in range(col1):
                    mul_arr[i][k] += m_a[i][j] * m_b[j][k]

    return mul_arr


