#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    colm = len(matrix[0]) if rows > 0 else 0

    result = [[0] * colm for _ in range(rows)]

    for i in range(rows):
        for j in range(colm):
            result[i][j] = matrix[i][j] ** 2
    return result
