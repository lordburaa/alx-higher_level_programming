#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

m_a = [
        [1.2, 5.5, 6.2],
        [4.66, 12.3, -9.2]
        ]
m_b = [
        [5.0, 3.3],
        [-2.9, 4.4],
        [7.2, 4.4]
        ]
print(lazy_matrix_mul(m_a, m_b))
exit()
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6, 7]]))
