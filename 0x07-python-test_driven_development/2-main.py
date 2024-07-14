#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

try:
    matrix = [
        [2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e)

try:
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, "a"))
except Exception as e:
    print(e)

try:
    matrix = [
        [1, "2", 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, "a"))
except Exception as e:
    print(e)

print(matrix_divided())
print(matrix)
