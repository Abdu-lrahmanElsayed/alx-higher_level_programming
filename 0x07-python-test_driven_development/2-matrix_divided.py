#!/usr/bin/python3
"""This module is to divide all elements of a function"""


def matrix_divided(matrix, div):
    """the function to divide

        args:
            matrix: list of lists of integers
            div: a number to divide on

        raise:
            TypeError: if matrix indexs is not integers
            TypeError: if the matrix rows is not in the same size
            TypeErroe: if div not integer
            ZeroDivisionError: if div = 0
            """
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix ' +
                        '(list of lists) of integers/floats')
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix ' +
                            '(list of lists) of integers/floats')
        elif len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError('matrix must be a matrix ' +
                                '(list of lists) of integers/floats')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    div_matrix = [[round(i / div, 2) for i in row] for row in matrix]
    return div_matrix


if __name__ == "__main__":
    import doctest
    doctest.testmethod("tests/2-matrix_divided.txt")
