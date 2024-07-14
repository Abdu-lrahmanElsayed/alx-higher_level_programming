#!/usr/bin/python3
"""a function that multiplies 2 matrices by using the module NumPy

    To install it: pip3 install numpy==1.15.0"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
        if len(row) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError('m_b should contain only integers or floats')
        if len(row) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return np.dot(m_a, m_b)


if __name__ == "__main__":
    import doctest
    doctest.testmethod("tests/101-lazy_matrix_mul.txt")
