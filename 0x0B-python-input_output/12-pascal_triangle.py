#!/usr/bin/python3
"""A module for pascal_triangle function"""


def pascal_triangle(n):
    """a function that returns a list of lists of integers
        representing the Pascal’s triangle of n"""
    my_tri = [[1]]
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n <= 0:
        return []
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(my_tri[i-1][j-1] + my_tri[i-1][j])
        row.append(1)
        my_tri.append(row)
    return my_tri
