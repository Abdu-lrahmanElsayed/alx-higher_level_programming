#!/usr/bin/python3
"""Module"""


def matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
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
    mul_m = [
                [
                    sum(a * b for a, b in zip(m_a_row, m_b_col))
                    for m_b_col in zip(*m_b)
                ]
                for m_a_row in m_a
            ]
    return mul_m


if __name__ == "__main__":
    import doctest
    doctest.testmethod("tests/100-matrix_mul.txt")
